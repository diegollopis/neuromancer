from os import system as cmd
from time import sleep as timer

class Utils:
    
    def print_line(self, times: int):
        print('-' * times)

    def clear_screen(self):
        cmd('clear')

    def wait(self):
        timer(2)

    def print_options(self):
        title = 'NEUROMANCER 1.0'
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')
        self.print_line(len(title))
        print(title)
        self.print_line(len(title)) 
        for item in items[:7]:
            print(item) 
        self.print_line(len(title))
        print('>> Type commit type from above ("quit" to exit the program or "help" to know more about semantic commits)')
        return items

    def choose_option(self):
        options = self.print_options()
        option = input(": ").lower()
        while option not in options:
            option = input("Invalid option. Try again: ").lower()
        return option
