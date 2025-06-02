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
            VALUES (?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, (company, position, status, date_applied, notes))
            connection.commit()
            cursor.close()

            print("Application inserted successfully")