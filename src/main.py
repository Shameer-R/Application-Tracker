from datetime import datetime

import Database
import ui

internship_database_string = "../database/internship_database.db"
job_database_string = "../database/job_database.db"

current_string = None
current_database = None

# Determines whether we use internship or job database
def select_database():
    global current_database
    global current_string

    database_input = input("Select Database: \n1. Job Database\n2. Internship Database\n")
    if database_input == "1":
        current_string = job_database_string
        print("\nYou selected Job Database!\n")
    elif database_input == "2":
        current_string = internship_database_string
        print("\nYou selected Internship Database!\n")
    else:
        print("Invalid Input, try again")

    current_database = Database.Database(current_string)

# Prompts given to the user when the application starts
def starting_prompt():
    starting_input = input("Select Key: \n1. Add an application\n2. Update an application\n"
                           "3. Delete an application\n4. Launch UI")
    if starting_input == "1":
        add_application()
    elif starting_input == "2":
        update_application()
    elif starting_input == "3":
        remove_application()
    elif starting_input == "4":
        number_of_applications = current_database.getApplicationCount()
        if number_of_applications > 0:
            ui.main(current_string)
        else:
            print("\nNo applications, you must add one first. Try again.\n")
            starting_prompt()


ApplicationDictionary = {
    "company": None,
    "position": None,
    "status": None,
    "date_applied": None,
    "notes": None
}


# Transfer prompts to dictionary
def prompt_to_dictionary(prompt, field):
    new_prompt = input(prompt).replace(" ", "")  # Remove whitespace from prompt
    ApplicationDictionary[field] = new_prompt


# Input data from dictionary to database
def dictionary_to_database():
    current_database.insert_application(
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


def get_application_from_input():
    all_applications = current_database.get_all_companies()

    for i in range(len(all_applications)):
        print(f"{i} - {all_applications[i][0]}")

    selected_input = int(input("\nEnter Number: \n"))

    # Pull name of company from input
    selected_application = all_applications[selected_input][0]

    return selected_application


ApplicationList = ["company", "position", "status", "date_applied", "notes"]


def update_application():
    print("\nSelect number of application to update (Leave blank if none): ")

    selected_application = get_application_from_input()

    print(f"\nWhat field would you like to update for {selected_application}?\n")

    for i in range(len(ApplicationList)):
        print(f"{i} - {ApplicationList[i]}")

    selected_input = int(input("\nEnter Number: \n"))

    selected_field = ApplicationList[selected_input]

    updated_field = input(f"\nEnter your desired change for {selected_application}'s {selected_field}: ")

    current_database.update_field(selected_application, selected_field, updated_field)


def remove_application():
    print("\nSelect number of application to remove (Leave blank if none):")

    selected_application = get_application_from_input()

    current_database.delete_application(selected_application)


def main():
    select_database()
    starting_prompt()

if __name__ == "__main__":
    main()
