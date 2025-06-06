import sqlite3

create_table_query = '''
CREATE TABLE IF NOT EXISTS Applications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company TEXT NOT NULL,
  position TEXT NOT NULL,
  status TEXT NOT NULL,
  date_applied DATE NOT NULL,
  notes TEXT
);'''
class Database:
    def __init__(self, database_string):

        self.DATABASE_STRING = database_string

        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()

    def insert_application(self, company, position, status, date_applied, notes):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            insert_query = '''
            INSERT INTO Applications (company, position, status, date_applied, notes)
            VALUES (?, ?, ?, ?, ?);
            '''
            cursor.execute(insert_query, (company, position, status, date_applied, notes,))
            connection.commit()
            cursor.close()

            print("Application inserted successfully")

    def get_all_companies(self):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            select_query = '''
            SELECT company FROM Applications;'''

            cursor.execute(select_query)

            all_applications = cursor.fetchall()

            cursor.close()

            return all_applications

    def get_all_applications(self):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            select_query = '''
            SELECT * FROM Applications;'''

            cursor.execute(select_query)

            all_applications = cursor.fetchall()
            cursor.close()

            return all_applications

    def delete_application(self, company_name):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            delete_query = '''
            DELETE FROM Applications 
            WHERE company = ?;'''

            cursor.execute(delete_query, (company_name,))
            connection.commit()
            cursor.close()

            print(f"{company_name} has been deleted")

    def getApplicationCount(self):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            count_query = '''
            SELECT COUNT (*) FROM Applications;'''
            cursor.execute(count_query)

            number_of_applications = cursor.fetchone()[0]
            cursor.close()
            connection.commit()
            return number_of_applications

    def update_field(self, company_name, field_name, new_field_value):
        with sqlite3.connect(self.DATABASE_STRING) as connection:
            cursor = connection.cursor()
            update_query = f'''
            UPDATE Applications
            SET {field_name} = ? 
            WHERE company = ?;
            '''

            cursor.execute(update_query, (new_field_value, company_name,))
            connection.commit()
            cursor.close()

            print("Updated field successfully")