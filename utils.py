from os import system as cmd
from time import sleep as timer

class Utils:
    
    def print_line(self):
        print("-------------")

    def clear_screen(self):
        cmd('clear')

    def wait(self):
        timer(2)

    def print_options(self):
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')
        self.print_line()
        print('NEUROMANCER 1.0')
        self.print_line() 
        for item in items[:7]:
            print(item) 
        self.print_line()
        return items

    def choose_option(self):
        options = self.print_options()
        option = input(": ").lower()
        while option not in options:
            option = input("Opção não permitida. Digite novamente: ").lower()
        return option
