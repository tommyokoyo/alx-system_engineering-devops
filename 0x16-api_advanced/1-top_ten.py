#!/usr/bin/python3
"""
Queries for titles of the first 10 hotspots
"""

import requests

def top_ten(subreddit):
    base_url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    req_headers = {"user-agent": " Apple-safari"}
    try:
        data = requests.get(base_url, headers=req_headers).json()
        hot_posts = data['data']['children']
        for posts in hot_posts:
            print(posts['data']['title'])

    except Exception:
        print("None")
