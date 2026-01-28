def show_tasks():
    file = open("tasks.txt", "r")
    tasks = file.read()
    print("Your Tasks:")
    print(tasks)
    file.close()

show_tasks()
