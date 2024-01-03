#!/usr/bin/python3
"""Returns TODO list information about a given employee ID."""
import sys
import requests as requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comps = [title.get("title") for title in todos if title.get("comps") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(comps), len(todos)))
    [print("\t {}".format(title)) for title in comps]
