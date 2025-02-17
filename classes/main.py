from classes.utils import Utils
from classes.git_actions import GitAction
from classes.helper import Helper

class Controller:

    @classmethod
    def show_helper(cls):
        Utils.clear_screen()
        Helper().print_helper()
        _ = input('Press "Enter" to exit: ')
        cls.run()

    @classmethod
    def format_commit_message(cls, option: str, message: str):
        return f'{option}: {message}'

    @classmethod
    def execute_git_steps(cls, option: str):
        message_confirmation_options = ['y', 'n', 'quit']
        minimum_length_commit_message = 12

        commit_message = input('\n>> Commit message: ').lower()

        if commit_message == 'quit':
            cls.run()
            return

        while not commit_message.strip() or len(commit_message) <= minimum_length_commit_message:
            commit_message = input(
                f'\n>> Commit message needs at least {str(minimum_length_commit_message)} characters. Try again: '
            ).lower()

        commit_message_formatted = cls.format_commit_message(option, commit_message)

        commit_message_confirmation = input(f'\n>> "{commit_message_formatted}". Confirm? (y/n): ').lower()

        while commit_message_confirmation not in message_confirmation_options :
            commit_message_confirmation = input(f'Wrong input. Try again (y/n): ').lower()

        if commit_message_confirmation == 'y':
            GitAction.do_git_steps(commit_message_formatted)
        elif commit_message_confirmation == 'quit':
            cls.run()
        else:
            cls.execute_git_steps(option)

    @classmethod
    def run(cls):
        is_git = GitAction.check_is_git_detected()
        are_changes = GitAction.check_changed_files()
        
        if not is_git:
            print('\nGit not found!\n')
            return

        if not are_changes:
            print('\nThere are no modifications in this repository!\n')
            return

        Utils.clear_screen()
        option = Utils.choose_option()

        if option == 'quit':
            Utils.clear_screen()
            quit()
        elif option == 'help':
            cls.show_helper()
        else:
            cls.execute_git_steps(option)
            