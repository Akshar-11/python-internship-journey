import json

# Load existing applications from file
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

# Save applications back to file
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Add a new internship application
def add_application():
    data = load_data()

    company = input("Enter company name: ")
    role = input("Enter role: ")
    location = input("Enter location: ")

    application = {
        "company": company,
        "role": role,
        "location": location,
        "status": "Applied"
    }

    data.append(application)
    save_data(data)

    print("✅ Application saved successfully!")



# Note: Ensure that a 'data.json' file exists in the same directory as this script.
# If it doesn't exist, create an empty list in 'data.json' like this: []
# code will not run correctly without it.
# will learn more about file handling in upcoming days and fix this limitation.
# it took some help to figure this out :)

# On Day 8, I tried to add a loop to allow multiple entries without restarting the program.
# Also, I wanted to add a feature to view all saved applications after adding a new one.
# Here's the updated code with those features:

# View all applications
def view_applications():
    data = load_data()

    if len(data) == 0:
        print("⚠️ No applications found.\n")
        return

    print("\n Your Applications:")
    print("--------------------")
                                                #index adds numbering to the list
    for index, app in enumerate(data, start=1): #enumerate takes a list and gives number, item pairs. it does the counter automatically.
                                                # start == 1 makes numbering start from 1 instead of 0
        print(f"{index}. {app['company']} | {app['role']} | {app['location']} | {app['status']}")

    print()

# Main program loop
def main():
    while True:
        print("==== Internship Tracker ====")
        print("1. Add application")
        print("2. View applications")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start the program
main()
