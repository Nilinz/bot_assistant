from .address_book_main import address_book_main_func
from .notes_main import notes_main_func
from .sort_main import sort_main_func
from rich import print as rprint
from abc import ABC, abstractmethod

TEXT_COLOR = {
    "red": "\033[31m",
    "green": "\033[32m",
    "reset": "\033[0m"
}
class UserInterface(ABC):
    @abstractmethod
    def run(self):
        pass

class AddressBookUI(UserInterface):
    def run(self):
        address_book_main_func()

class NotesUI(UserInterface):
    def run(self):
        notes_main_func()

class SortingFilesUI(UserInterface):
    def run(self):
        arg = input("Enter the path to sort files: ")
        confirm_input = input(f"Are you sure you want to sort all the files in ({arg}) path !? (y/n): ")
        if confirm_input.lower() == 'y':
            sort_main_func(arg)
        elif confirm_input.lower() == 'n':
            print('Operation canceled.')
        else:
            print('Incorrect input!')

class ConsoleBot:
    def __init__(self):
        self.interfaces = {
            'addressbook': AddressBookUI(),
            'notebook': NotesUI(),
            'sorting_files': SortingFilesUI(),
        }
    def run(self):
        print("\nHi, I'm your personal helper!")

        while True:
            rprint("\nYou can run: \n-'addressbook'\n-'notebook' \n-'sorting_files *path*'\n\nOr close your personal helper by 'close' or 'exit'")
            choose_program_inp = input('\nChoose the program >>> ')

            if choose_program_inp in ['close', 'exit']:
                print('\nGood bye!')
                break

            if choose_program_inp in self.interfaces:
                self.interfaces[choose_program_inp].run()
            else:
                print('Incorrect command!')

if __name__ == "__main__":
    bot = ConsoleBot()
    bot.run()


