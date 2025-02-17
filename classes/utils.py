from os import system as cmd
from time import sleep as timer

class Utils:

    @classmethod
    def print_line(cls, times: int):
        print('-' * times)

    @classmethod
    def clear_screen(cls):
        cmd('clear')

    @classmethod
    def wait(cls):
        timer(1)

    @classmethod
    def print_current_directory(cls):
        cmd('pwd')

    @classmethod
    def print_current_branch(cls):
        cmd('git branch --show-current')

    @classmethod
    def print_repo_remote_address(cls):
        cmd('git config --get remote.origin.url')

    @classmethod
    def print_repo_infos(cls):
        cls.print_current_directory()
        cls.print_repo_remote_address()
        cls.print_current_branch()

    @classmethod
    def print_options(cls):
        title = 'NEUROMANCER 1.0'
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')
        cls.print_repo_infos()
        cls.print_line(len(title))
        print(title)
        cls.print_line(len(title))
        for item in items[:7]:
            print(item) 
        cls.print_line(len(title))
        print('>> "quit" to exit or "help" to know more about semantic commits')
        return items

    @classmethod
    def choose_option(cls):
        options = cls.print_options()
        option = input("\n>> Commit type: ").lower()
        while option not in options:
            option = input(">> Invalid option. Try again: ").lower()
        return option
