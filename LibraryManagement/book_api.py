'''
This python file is used to collect AI book information using the Book API and
store in a database.
'''

import requests
from Database.database import LibraryDatabase

def get_top_books(api_key):
    book_database = LibraryDatabase()
    book_database.create_book_table()

    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": "Artificial Intelligence",  # Retrieve top books with Artificial Intelligence topics
        "orderBy": "newest",  # Sorted by newest books
        "maxResults": 20,  # Limit to the top 20 results
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

                cursor.execute('INSERT INTO BookTable (Title, Author, PublishDate) VALUES (?, ?, ?)', (title, ', '.join(authors), published_date))
                conn.commit()
    else:
        print(f"Error: {response.status_code}")

# Google Books API key
api_key = 'AIzaSyDL65aTCAjdBM0ogHGMbLRFcYRuXbA6iTU'

get_top_books(api_key)

