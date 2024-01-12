'''
This python file is used to collect AI book information using the Book API and
store in a database.
'''

import requests
import random
from Database.database import LibraryDatabase

def get_top_books(api_key):
    book_database = LibraryDatabase()
    book_database.create_book_table()

    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": "Artificial Intelligence",  # Retrieve top books with Artificial Intelligence topics
        "orderBy": "newest",  # Sorted by newest books
        "maxResults": 10,  # Limit to the top 10 results
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        books = data.get("items", [])

        with book_database.connect_to_database() as conn:
            cursor = conn.cursor()

            for book_data in books:
                volume_info = book_data.get("volumeInfo", {})
                title = volume_info.get("title", "N/A")
                authors = volume_info.get("authors", ["N/A"])
                published_date = volume_info.get("publishedDate", "N/A")
                bookID = volume_info.get("industryIdentifiers", [{"type": "ISBN_13", "identifier": "N/A"}])[0]["identifier"] # Uses ISBN as the BookID

                # Generate 13 random numbers if the BookID or ISBN is N/A
                if bookID == "N/A":
                    bookID = str(random.randint(10**(12), 10**(13) - 1))

                cursor.execute('INSERT INTO BookTable (BookID, Title, Author, PublishDate) VALUES (?, ?, ?, ?)', (bookID, title, ', '.join(authors), published_date))
                conn.commit()
    else:
        print(f"Error: {response.status_code}")

# Google Books API key
api_key = 'AIzaSyDL65aTCAjdBM0ogHGMbLRFcYRuXbA6iTU'

get_top_books(api_key)

