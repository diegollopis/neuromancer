from classes.utils import Utils
from classes.git_actions import GitAction
from classes.helper import Helper
import sys

class Controller:

    commit_option: str = ''
    commit_message: str = ''

    @classmethod
    def print_app_title(cls, title):
        Utils.print_line(len(title))
        print(title)
        Utils.print_line(len(title))

    @classmethod
    def print_options(cls):
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')
        cls.print_app_title('NEUROMANCER 1.0')
        for item in items[:7]:
            print(item)
        Utils.print_line(len('NEUROMANCER 1.0'))
        print('>> "quit" to exit or "help" to know more about semantic commits')
        return items

    @classmethod
    def choose_option(cls):
        options = cls.print_options()
        option = input("\n>> Commit type: ").lower()
        while option not in options:
            option = input(">> Invalid option. Try again: ").lower()
        cls.commit_option = option
        return option

    @classmethod
    def show_helper(cls):
        Utils.clear_screen()
        Helper().print_helper()
        _ = input('Press "Enter" to exit: ')
        cls.run()

    @classmethod
    def format_commit_message(cls):
        return f'{cls.commit_option}: {cls.commit_message}'

    @classmethod
    def check_message(cls):
        message_confirmation_options = ['y', 'n', 'quit']
        minimum_length_commit_message = 12

        message = input('\n>> Commit message: ').lower()

        if message == 'quit':
            cls.run()
            return

        while not message.strip() or len(message) <= minimum_length_commit_message:
            message = input(
                f'\n>> Commit message needs at least {str(minimum_length_commit_message)} characters. Try again: '
            ).lower()

        cls.commit_message = message

        commit_message_formatted = cls.format_commit_message()

        commit_message_confirmation = input(f'\n>> "{commit_message_formatted}". Confirm? (y/n): ').lower()

        while commit_message_confirmation not in message_confirmation_options:
            commit_message_confirmation = input(f'Wrong input. Try again (y/n): ').lower()
        return commit_message_confirmation

    @classmethod
    def execute_git_steps(cls):
        commit_message_formatted = cls.format_commit_message()
        commit_message_confirmation = cls.check_message()

        if commit_message_confirmation == 'y':
            GitAction.do_git_steps(commit_message_formatted)
        elif commit_message_confirmation == 'quit':
            cls.run()
        else:
            cls.execute_git_steps()

    @classmethod
    def splash_and_go(cls):
        argument_list = sys.argv
        if len(argument_list) > 1:
            cls.commit_option = sys.argv[1]
            cls.commit_message = ' '.join(sys.argv[2:])
            message_formatted = cls.format_commit_message()
            GitAction.do_git_steps(message_formatted)

    @classmethod
    def run(cls):
        is_git = GitAction.check_is_repo_git()
        are_changes = GitAction.check_changed_files()
        
        if not is_git:
            print('\nGit not found!\n')
            return

        if not are_changes:
            print('\nThere are no modifications in this repository!\n')
            return

        if len(sys.argv) > 1:
            cls.splash_and_go()
        else:
            Utils.clear_screen()
            option = cls.choose_option()

            if option == 'quit':
                Utils.clear_screen()
                quit()
            elif option == 'help':
                cls.show_helper()
            else:
                cls.execute_git_steps()
            