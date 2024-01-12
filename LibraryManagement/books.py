from Database.database import LibraryDatabase

class Books:
    def __init__(self):
        self.library_database = LibraryDatabase()

    def __str__(self):
        return '''\nPlease select a number:
                1. Display all books
                2. Add books
                3. Remove books
                4. Update books\n'''
    
    def options(self):
        self.options = int(input("Choose a number: "))
        if self.options == 1:
            self.list_books()
        if self.options == 2:
            self.add_books()
        if self.options == 3:
            self.remove_books()
        if self.options == 4:
            self.update_books()

    def list_books(self):
    
        with self.library_database.connect_to_database() as conn:
            self.cursor = conn.cursor()

            self.cursor.execute('SELECT * FROM BookTable')
            all_books = self.cursor.fetchall()
            
            for book in all_books:
                print(f'BookID: {book[0]}')
                print(f"Title: {book[1]}")
                print(f"Author: {book[2]}")
                print(f"Published Date: {book[3]}\n")
        
        self.library_database.close_connection()

    def add_books(self):
        
        try: 
            with self.library_database.connect_to_database() as conn:

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
            print(f'Error: ' + str(e))


    def remove_books(self):
        
        try:
            with self.library_database.connect_to_database() as conn:
                self.cursor = conn.cursor()

                bookID_to_remove = input("Enter the ID of the book you want to remove: ")

                self.cursor.execute(f'DELETE FROM BookTable WHERE Title = "{bookID_to_remove}"')
                print(f'Book "{bookID_to_remove}" removed successfully!')

        except Exception as e:
            print(f'Error: ' + str(e))

        self.library_database.close_connection()

    def update_books(self):
        
        try:
            with self.library_database.connect_to_database() as conn:
                self.cursor = conn.cursor()

                bookID_to_update = input("Enter the ID of the book you want to update: ")

                # Display the current data for the memberID to be updated
                self.cursor.execute(f'SELECT * FROM BookTable WHERE BookID = "{bookID_to_update}"')
                book_data = self.cursor.fetchall()

                # Convert member data into a list of list because it is a list of tuples
                book_data_list = [list(row) for row in book_data]

                for book in book_data_list:
                    print(f'BookID: {book[0]}')
                    print(f"Title: {book[1]}")
                    print(f"Author: {book[2]}")
                    print(f"Published Date: {book[3]}\n")

                new_title = input("Enter the book title (leave empty to keep the current data): ")    
                new_author = input("Enter the author (leave empty to keep the current data): ")
                new_publishDate = input("Enter the publish date (leave empty to keep the current data): ")

                if new_title:
                    self.cursor.execute('UPDATE BookTable SET Title = ? WHERE BookID = ?', (new_title, bookID_to_update))
                if new_author:
                    self.cursor.execute('UPDATE BookTable SET Author = ? WHERE BookID = ?', (new_author, bookID_to_update))
                if new_publishDate:
                    self.cursor.execute('UPDATE BookTable SET PublishDate = ? WHERE BookID = ?', (new_publishDate, bookID_to_update))

                conn.commit()
                print(f'Book with ID {bookID_to_update} update successfully!')

        except Exception as e:
            print(f'Error: ' + str(e))

