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
