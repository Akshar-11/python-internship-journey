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

# Run the program
add_application()

# Note: Ensure that a 'data.json' file exists in the same directory as this script.
# If it doesn't exist, create an empty list in 'data.json' like this: []
# code will not run correctly without it.
# will learn more about file handling in upcoming days and fix this limitation.
# it took some help to figure this out :)
