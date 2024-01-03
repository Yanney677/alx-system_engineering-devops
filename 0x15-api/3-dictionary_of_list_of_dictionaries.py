#!/usr/bin/python3
"""Export all employees information to JSON format."""
import requests
import json

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()
    
    json_filename = "todo_all_employees.json"

    with open("json_filename", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(base_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
