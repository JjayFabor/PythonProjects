'''
    Library Management System
'''

from books import Books

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

        if self.options == 2:
            print(self.books)
            self.books.options()

    def library(self):
        pass


if __name__ == "__main__":
    menu = Menu()
    print(menu)
    menu.options()