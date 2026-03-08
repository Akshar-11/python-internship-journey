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

#On day 10, I wanted to add a feature to delete an application from the tracker.
#this completes the CRUD (Create, Read, Update, Delete) functionality for the internship tracker.
# Delete application

def delete_application():
    data = load_data()

    if not view_applications():
        return

    try:
        choice = int(input("Select application number to delete: "))
        if choice < 1 or choice > len(data):
            print("❌ Invalid selection.\n")
            return
    except:
        print("❌ Please enter a valid number.\n")
        return

    confirm = input("Are you sure you want to delete this application? (y/n): ").lower()

    if confirm == "y":
        deleted = data.pop(choice - 1)
        save_data(data)
        print(f"🗑️ Deleted application for {deleted['company']}.\n")
    else:
        print("❌ Deletion cancelled.\n")

# On day 11, I wanted to add a filter feature to view applications based on their status.
#this function allows users to easily see which applications are in which stage of the process, improving the overall user experience.

# Filter applications by status
def filter_by_status():
    data = load_data()

    print("\nFilter by status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Offer")
    print("4. Rejected")

    choice = input("Choose status (1-4): ")

    status_map = {
        "1": "Applied",
        "2": "Interview",
        "3": "Offer",
        "4": "Rejected"
    }

    if choice not in status_map:
        print("❌ Invalid choice.\n")
        return

    filtered = [app for app in data if app["status"] == status_map[choice]]

    print(f"\n📊 Showing {status_map[choice]} applications:")
    view_applications(filtered)


# Main menu
def main():
    while True:
        print("==== Internship Tracker ====")
        print("1. Add application")
        print("2. View applications")
        print("3. Update application status")
        print("4. Delete Application")
        print("5. Filter by status")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications(show_index=False)
        elif choice == "3":
            update_status()
        elif choice == "4" :
            delete_application()
        elif choice == "5":
            filter_by_status()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Start program
main()
