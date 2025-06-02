import database.Database
from database.Database import Database

application_database = database.Database.Database()
def starting_prompt():
    starting_input = input("Select Key: \n1. Add an application\n2. Update an application\n")
    if starting_input == "1":
        add_application()
    elif starting_input == "2":
        update_application()

def add_application():
    pass
def update_application():
    pass

def main():
    starting_prompt()


if __name__ == "__main__":
    main()