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
    def __init__(self):
        with sqlite3.connect('../database/application_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
            print("Application Database intialized successfully")

    def insert_application(self, company, position, status, date_applied, notes):
        with sqlite3.connect('../database/application_database.db') as connection:
            cursor = connection.cursor()
            insert_query = '''
            INSERT INTO Applications (company, position, status, date_applied, notes)
            VALUES (?, ?, ?, ?, ?);
            '''
            cursor.execute(insert_query, (company, position, status, date_applied, notes,))
            connection.commit()
            cursor.close()

            print("Application inserted successfully")

    def get_all_applications(self):
        with sqlite3.connect('../database/application_database.db') as connection:
            cursor = connection.cursor()
            select_query = '''
            SELECT company FROM Applications;'''

            cursor.execute(select_query)

            all_applications = cursor.fetchall()

            cursor.close()

            return all_applications

    def delete_application(self, company_name):
        with sqlite3.connect('../database/application_database.db') as connection:
            cursor = connection.cursor()
            delete_query = '''
            DELETE FROM Applications 
            WHERE company = ?;'''

            cursor.execute(delete_query, (company_name,))
            connection.commit()
            cursor.close()

            print(f"{company_name} has been deleted")