def add_task(task):
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()

task = input("Enter task: ")
add_task(task)
print("Task saved!")
