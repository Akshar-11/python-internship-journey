age = int(input("Age: "))
citizen = input("Citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")
