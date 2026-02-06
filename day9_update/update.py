import json

# Load data
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Add application
def add_application():
    data = load_data()

    company = input("Company name: ")
    role = input("Role: ")
    location = input("Location: ")

    application = {
        "company": company,
        "role": role,
        "location": location,
        "status": "Applied"
    }

    data.append(application)
    save_data(data)

    print("✅ Application added!\n")

# View applications
def view_applications(show_index=True): 
    data = load_data()

    if len(data) == 0:
        print("⚠️ No applications found.\n")
        return False

    print("\n📄 Your Applications:")
    print("--------------------")

    for index, app in enumerate(data, start=1):
        if show_index:
            print(f"{index}. {app['company']} | {app['role']} | {app['location']} | {app['status']}")
        else:
            print(f"{app['company']} | {app['role']} | {app['location']} | {app['status']}")

    print()
    return True

#on day 9, I want to add the ability to update the status of an application.
#also, I want to improve the view function to optionally show or hide the index numbers.
#try enhancing the user experience with clear prompts and error handling.

# Update application status
def update_status():
    data = load_data()

    if not view_applications():
        return

    try:
        choice = int(input("Select application number to update: "))
        if choice < 1 or choice > len(data):
            print("❌ Invalid selection.\n")
            return
    except:
        print("❌ Please enter a valid number.\n")
        return

    print("\nChoose new status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Offer")
    print("4. Rejected")

    status_choice = input("Enter choice (1-4): ")

    status_map = {
        "1": "Applied",
        "2": "Interview",
        "3": "Offer",
        "4": "Rejected"
    }

    if status_choice not in status_map:
        print("❌ Invalid status.\n")
        return

    data[choice - 1]["status"] = status_map[status_choice]
    save_data(data)

    print("✅ Status updated successfully!\n")

# Main menu
def main():
    while True:
        print("==== Internship Tracker ====")
        print("1. Add application")
        print("2. View applications")
        print("3. Update application status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications(show_index=False)
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start program
main()
