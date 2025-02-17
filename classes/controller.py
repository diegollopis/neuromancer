import sys
from classes.helper import Helper
from classes.git_actions import GitAction

class Controller:

    commit_option: str = ''
    commit_message: str = ''
    items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')

    @classmethod
    def format_commit_message(cls):
        return f'{cls.commit_option}: {cls.commit_message}'

    @classmethod
    def show_helper(cls):
        Helper.print_helper()

    @classmethod
    def splash_and_go(cls):
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
            if sys.argv[1] == 'help':
                cls.show_helper()
            else:
                cls.commit_option = sys.argv[1]
                cls.commit_message = ' '.join(sys.argv[2:])
                message_formatted = cls.format_commit_message()
                confirm = input(f'\n"{message_formatted}". Confirm? [y/n]: ').lower()
                while confirm != 'y' and confirm != 'n':
                    confirm = input('\nWrong input. Try again [y/n]: ').lower()
                if confirm == 'y':
                    GitAction.do_git_steps(message_formatted)
                else:
                    print()
                    return
        else:
            print('\nPlease add a commit message!\n')
            return
            