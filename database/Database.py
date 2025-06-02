import sqlite3

create_table_query = '''
CREATE TABLE IF NOT EXISTS Application (
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
