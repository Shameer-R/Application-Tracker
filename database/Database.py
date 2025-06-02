import sqlite3
class Database:
    def Connect(self):
        connection = sqlite3.connect('application_database.db')
        cursor = connection.cursor()

        return cursor
