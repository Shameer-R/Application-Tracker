from datetime import datetime

import database.Database
from database.Database import Database

application_database = database.Database.Database()

# Prompts given to the user when the application starts
def starting_prompt():
    starting_input = input("Select Key: \n1. Add an application\n2. Update an application\n3. Delete an application\n")
    if starting_input == "1":
        add_application()
    elif starting_input == "2":
        update_application()
    elif starting_input == "3":
        remove_application()


ApplicationDictionary = {
    "company": None,
    "position": None,
    "status": None,
    "date_applied": None,
    "notes": None
}

# Transfer prompts to dictionary
def prompt_to_dictionary(prompt, field):
    new_prompt = input(prompt).replace(" ", "") # Remove whitespace from prompt
    ApplicationDictionary[field] = new_prompt

# Input data from dictionary to database
def dictionary_to_database():
    application_database.insert_application(
        ApplicationDictionary["company"], ApplicationDictionary["position"],
        ApplicationDictionary["status"], ApplicationDictionary["date_applied"],
        ApplicationDictionary["notes"]
    )

# Get date in YYYY-MM-DD format
def format_todays_date():
    today = str(datetime.today())
    today_format = today.split(" ")
    return today_format[0]

# Start process for adding application
def add_application():
    print("\n--- Enter Application Information --- ")
    prompt_to_dictionary("Enter Company: ", "company")
    prompt_to_dictionary("Enter Position: ", "position")
    prompt_to_dictionary("Enter Notes (Leave blank if none): ", "notes")

    ApplicationDictionary["status"] = "Pending"
    ApplicationDictionary["date_applied"] = format_todays_date()

    dictionary_to_database()

def update_application():
    pass

def remove_application():
    application_database.get_all_applications()

def main():
    starting_prompt()


if __name__ == "__main__":
    main()