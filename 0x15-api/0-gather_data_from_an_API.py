#!/usr/bin/python3
"""Returns TODO list information about a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos_url = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos_url if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos_url)))
    [print("\t {}".format(c)) for c in completed]
