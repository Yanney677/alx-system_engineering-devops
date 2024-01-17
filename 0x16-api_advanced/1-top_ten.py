#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    resp = requests.get('https://www.reddit.com/r/{:}/hot.json?limit=10'.format(
        subreddit), headers=headers, allow_redirects=False)
    if resp.status_code < 300:
        json = resp.json()
        data_dict = json.get('data')
        h_list = data_dict.get('children')
        for post in h_list:
            sub_data_dict = post.get('data')
            print(sub_data_dict.get('title'))
    else:
        print(None)
