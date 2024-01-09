from Database.database import BookDatabase

class Books:
    def __init__(self):
        self.book_database = BookDatabase()

    def __str__(self):
        return '''\nPlease select a number:
                1. Display all books
                2. Add books
                3. Remove books\n'''
    
    def options(self):
        self.options = int(input("Choose a number: "))
        if self.options == 1:
            self.list_books()
        if self.options == 2:
            self.add_books()
        if self.options == 3:
            pass

    def list_books(self):
    
        with self.book_database.connect_to_database() as conn:
            self.cursor = conn.cursor()

            self.cursor.execute('SELECT * FROM BookTable')
            all_books = self.cursor.fetchall()
            
            for book in all_books:
                print(f"Title: {book[0]}")
                print(f"Author: {book[1]}")
                print(f"Published Date: {book[2]}\n")
        
        self.book_database.close_connection()

    def add_books(self):
        
        try: 
            with self.book_database.connect_to_database() as conn:

                isBookAdded = False
                self.cursor = conn.cursor()

                title = input("Enter title of the book: ")
                author = input("Enter author of the book: ")
                published_date = input("Enter the published date of the book (yyyy-mm-dd): ")

                self.cursor.execute(f'INSERT INTO BookTable (Title, Author, PublishDate) VALUES (?, ?, ?)', (title, author, published_date))
                conn.commit()
                isBookAdded = True

            if isBookAdded:
                print("Book Added Successfully!")
            else:
                print("Book not added!")

        except Exception as e:
            print("Error: " + str(e))

    def remove_books(self):
        pass

    def borrow_books(self):
        pass
