#!/usr/bin/python3
"""Returns TODO list information about a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in todos if t.get("comp") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(comp), len(todos)))
    [print("\t {}".format(c)) for c in comp]
