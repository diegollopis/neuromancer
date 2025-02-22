import sys
from classes.helper import Helper
from classes.git_action import GitAction

class Controller:

    @classmethod
    def format_commit_message(cls, option: str, message: str):
        return f'{option}: {message}'

    @classmethod
    def print_message(cls, text: str):
        print()
        print(text)
        print()

    @classmethod
    def show_helper(cls):
        Helper.print_helper()

    @classmethod
    def confirm_message_and_do_git_steps_or_cancel(cls, message: str):
        confirm_options = ['n', 'y']

        confirm = input(f'\n"{message}". Confirm? [y/n]: ').lower()
        while confirm not in confirm_options:
            confirm = input('\nWrong input. Try again [y/n]: ').lower()
        if confirm == 'y':
            GitAction.do_git_steps(message)
        else:
            cls.print_message('Operation cancelled.')

    @classmethod
    def main(cls):
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore')

        is_git = GitAction.check_is_repo_git()
        are_changes = GitAction.check_changed_files()
        
        if not is_git:
            cls.print_message('Git not found!')
            return

        if not are_changes:
            cls.print_message('There are no modifications in this repository!')
            return

        if len(sys.argv) < 3:
            print(f'\nYou need to add a commit message!\n')
            return

        if len(sys.argv) > 1:
            if sys.argv[1] == 'help':
                cls.show_helper()
            elif sys.argv[1] not in items:
                print(f'\nCommit option is not valid! Only options below are available.\n\n{items}\n')
            else:
                commit_message = cls.format_commit_message(option= sys.argv[1], message= ' '.join(sys.argv[2:]))
                cls.confirm_message_and_do_git_steps_or_cancel(message= commit_message)
            