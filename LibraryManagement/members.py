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

                self.cursor.execute('SELECT MAX(MemberID) FROM MemberTable')
                max_id = self.cursor.fetchone()[0]

                # Generate new ID
                new_id = 20240001 if max_id is None else int(max_id) + 1
                
                memberID = last_name.lower() + str(new_id)
                
                self.cursor.execute(f'''
                        INSERT INTO MemberTable (MemberID, First_Name, Last_Name, Phone, Email, Address) VALUES (?, ?, ?, ?, ?, ?)
                    ''', (memberID, first_name, last_name, phone_number, email, address))
                conn.commit()
                print(f'Member added successfully.')

        except Exception as e:
            print(f'Error: {str(e)}')

    def remove_member(self):
        try:
            with self.library_database.connect_to_database() as conn:
                self.cursor = conn.cursor()

                memberID_to_delete = input("Enter the member ID to delete: ")

                self.cursor.execute(f'DELETE FROM MemberTable WHERE MemberID = "{memberID_to_delete}"')
                print(f'Member "{memberID_to_delete}" removed successfully!')

        except Exception as e:
            print(f'Error: ' + str(e))

        self.library_database.close_connection()


    def update_member(self):
        try: 
            with self.library_database.connect_to_database() as conn:
                self.cursor = conn.cursor()

                memberID_to_update = input("Enter the member ID to update: ")

                # Display the current data for the memberID to be updated
                self.cursor.execute(f'SELECT * FROM MemberTable WHERE MemberID = "{memberID_to_update}"')
                member_data = self.cursor.fetchall()

                # Convert member data into a list of list because it is a list of tuples
                member_data_list = [list(row) for row in member_data]

                for member in member_data_list:
                    print(f'\nMember ID: {member[0]}')
                    print(f'First Name: {member[1]}')
                    print(f'Last Name: {member[2]}')
                    print(f'Phone Number: {member[3]}')
                    print(f'Email: {member[4]}')
                    print(f'Address: {member[5]}\n')
                
                # Get new member data from the user
                new_firstName = input("Enter your first name (leave empty to keep current data): ")
                new_lastName = input("Enter your last name (leave empty to keep current data): ")
                new_phone = input("Enter your phone (leave empty to keep current data): ")
                new_email = input("Enter your email address (leave empty to keep current data): ")
                new_address = input("Enter your address (leave empty to keep current data): ")

                # Update new member data if it is provided
                if new_firstName:
                    self.cursor.execute('UPDATE MemberTable SET First_Name = ? WHERE MemberID = ?', (new_firstName, memberID_to_update))
                if new_lastName:
                    self.cursor.execute('UPDATE MemberTable SET Last_Name = ? WHERE MemberID = ?', (new_lastName, memberID_to_update))
                if new_phone:
                    self.cursor.execute('UPDATE MemberTable SET Phone = ? WHERE MemberID = ?', (new_phone, memberID_to_update))
                if new_email:
                    self.cursor.execute('UPDATE MemberTable SET Email = ? WHERE MemberID = ?', (new_email, memberID_to_update))
                if new_address:
                    self.cursor.execute('UPDATE MemberTable SET Address = ? WHERE MemberID = ?', (new_address, memberID_to_update))

                conn.commit()
                print(f'\nMember with ID {memberID_to_update} updated successfully!')

        except Exception as e:
            print(f'Error: {str(e)}')
    