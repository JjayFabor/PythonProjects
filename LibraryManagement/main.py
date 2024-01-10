'''
    Library Management System
'''

from books import Books
from members import Members

class Menu:
    def __init__(self):
        pass

    def __str__(self):
        return '''
                \n 
                  ========================================
                ||                                        ||
                ||  Welcome to Library Management System  ||
                ||               for                      ||
                ||    Artificial Intelligence Books       ||
                ||                                        ||
                  ========================================
                \n

                Please select a number:
                1. Library
                2. Books
                3. Members
                '''
    
    def options(self):
        self.options = int(input("Choose a number: "))
        self.books = Books()
        self.members = Members()

        if self.options == 2:
            print(self.books)
            self.books.options()
        if self.options == 3:
            self.members.remove_member()

    def library(self):
        pass


if __name__ == "__main__":
    menu = Menu()
    print(menu)
    menu.options()