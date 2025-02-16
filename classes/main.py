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
    def do_repo_push(cls, option: str):
        message = input('\n>> Commit message: ')
        message_formatted = f'{option}: {message}'
        GitAction.do_git_steps(message_formatted)

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
            cls.do_repo_push(option)
            