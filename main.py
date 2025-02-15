from utils import Utils
from git_actions import GitAction
from helper import Helper

class Controller:

    action = GitAction()
    utils = Utils()

    def show_helper(self):
        self.utils.clear_screen()
        helper = Helper()
        helper.print_helper()
        _ = input('Press "Enter" to exit: ')
        self.run()

    def do_repo_push(self, option: str):
        message = input('Digite a mensagem do commit: ')
        message_formatted = f'{option}: {message}'
        self.action.do_git_steps(message_formatted)

    def run(self):
        is_git = self.action.check_git()
        are_changes = self.action.status()
        
        if not is_git:
            print('Não é um diretório git!')
            return 
        
        if not are_changes:
            print('Não há modificações no repo!')
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
            