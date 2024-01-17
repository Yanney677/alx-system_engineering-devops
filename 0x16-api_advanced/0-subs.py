#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The total number of subscribers. Returns 0 if the subreddit is not found.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

        if response.status_code == 404:
            return 0

        results = response.json().get("data")
        return results.get("subscribers", 0)

    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))
        return 0
