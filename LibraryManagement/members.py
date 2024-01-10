from Database.database import LibraryDatabase

class Members:
    def __init__(self):

        # initialize database
        self.library_database = LibraryDatabase()

    def add_member(self):
        self.library_database.create_member_table()

        try:
            with self.library_database.connect_to_database() as conn:
                self.cursor = conn.cursor()

                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                phone_number = input("Enter your phone number: ")
                email = input("Enter your email address: ")
                address = input("Enter your address: ")

                self.cursor.execute(f'''
                        INSERT INTO MemberTable (First_Name, Last_Name, Phone, Email, Address) VALUES (?, ?, ?, ?, ?)
                    ''', (first_name, last_name, phone_number, email, address))

        except Exception as e:
            print(f'Error: {str(e)}')

    def remove_member(self):
        pass

    def update_member(self):
        pass
    