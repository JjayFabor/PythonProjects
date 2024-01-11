import sqlite3
import os

class LibraryDatabase:
    def __init__(self, book_directory='Database', database_name='LibraryDatabase.db'):
        self.book_directory = book_directory
        self.database_name = database_name

        self.database_path = os.path.join(self.book_directory, self.database_name)

    def connect_to_database(self):
        self.conn = sqlite3.connect(self.database_path)
        return self.conn
    
    def create_book_table(self):
        self.cursor = self.connect_to_database()
        try:
            self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS BookTable (
                        Title TEXT,
                        Author TEXT,
                        PublishDate TEXT
                    );
                ''')
        except Exception as e:
            print(f'Error creating table: {e}')
        
        self.close_connection()
    
    def create_member_table(self):
        self.cursor = self.connect_to_database()
        try:
            self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS MemberTable 
                        ( id TEXT PRIMARY KEY,
                        MemberID TEXT,
                        First_Name TEXT NOT NULL, 
                        Last_Name TEXT, 
                        Phone TEXT, 
                        Email TEXT, 
                        Address TEXT);
                    ''')
        except Exception as e:
            print(f'Error creating table: {e}')
        
        self.close_connection()

    def close_connection(self):
        self.conn.close()

