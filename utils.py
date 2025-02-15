import os
import time

class Utils:
    
    def print_line(self):
        print("-------------")

    def clear_screen(self):
        os.system('clear')

    def wait(self):
        time.sleep(2)

    def choose_option(self):
        items = ('feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', 'help', 'quit')
        self.print_line()
        print('NEUROMANCER 1.0')
        self.print_line() 
        for item in items:
            print(item)
        self.print_line()
        option = input(": ").lower()
        while option not in items:
            option = input("Opção não permitida. Digite novamente: ").lower()
        return option
