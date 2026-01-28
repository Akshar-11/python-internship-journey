import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()

with open("todos.json", "w") as file:
    json.dump(todos, file, indent=4)
