from datetime import datetime

import database.Database
from database.Database import Database

application_database = database.Database.Database()
def starting_prompt():
    starting_input = input("Select Key: \n1. Add an application\n2. Update an application\n")
    if starting_input == "1":
        add_application()
    elif starting_input == "2":
        update_application()


ApplicationDictionary = {
    "company": None,
    "position": None,
    "status": None,
    "date_applied": None,
    "notes": None
}

def prompt_to_database(prompt, field):
    new_prompt = input(prompt).replace(" ", "") # Remove whitespace from prompt
    ApplicationDictionary[field] = new_prompt

def insert_data_into_database():
    application_database.insert_application(
        ApplicationDictionary["company"], ApplicationDictionary["position"],
        ApplicationDictionary["status"], ApplicationDictionary["date_applied"],
        ApplicationDictionary["notes"]
    )


def format_todays_date():
    today = str(datetime.today())
    today_format = today.split(" ")
    return today_format[0]

def add_application():
    print("\n--- Enter Application Information --- ")
    prompt_to_database("Enter Company: ", "company")
    prompt_to_database("Enter Position: ", "position")
    prompt_to_database("Enter Notes (Leave blank if none): ", "notes")

    ApplicationDictionary["status"] = "Pending"
    ApplicationDictionary["date_applied"] = format_todays_date()

    insert_data_into_database()

def update_application():
    pass

def main():
    starting_prompt()


if __name__ == "__main__":
    main()