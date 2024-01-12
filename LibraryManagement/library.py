class Library:
    def __init__(self):
        pass

    def __str__(self):
        return '''
            Please select a number:
            1. Borrow Books
            2. Return Books
            '''

    def options(self):
        self.options = int(input("Choose a number: "))
        if self.options == 1:
            self.borrow_books()
        if self.options == 2:
            self.return_books()
            
    def borrow_books(self):
        pass

    def return_books(self):
        pass