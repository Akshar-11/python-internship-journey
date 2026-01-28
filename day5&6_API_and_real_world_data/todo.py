import requests

def fetch_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = response.json()

    for todo in todos[:10]:
        status = "✅" if todo["completed"] else "❌"
        print(todo["id"], ":", todo["title"], status)

fetch_todos()
