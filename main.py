from utils import Utils
from git_actions import GitAction
from helper import Helper

class Controller:

    action = GitAction()
    utils = Utils()

    def show_helper(self):
        self.utils.clear_screen()
        Helper().print_helper()
        _ = input('Press "Enter" to exit: ')
        self.run()

    def do_repo_push(self, option: str):
        print()
        message = input('Commit message: ')
        message_formatted = f'{option}: {message}'
        print()
        self.action.do_git_steps(message_formatted)

    def run(self):
        is_git = self.action.check_is_git_detected()
        are_changes = self.action.check_changed_files()
        
        if not is_git:
            print('Git not found!')
            return 
        
        if not are_changes:
            print('There are no modifications in this repository!')
            return

        self.utils.clear_screen()
        option = self.utils.choose_option()

        if option == 'quit':
            self.utils.clear_screen()
            quit()
        elif option == 'help':
            self.show_helper()
        else:
            self.do_repo_push(option)
            