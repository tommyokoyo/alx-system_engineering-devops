#!/usr/bin/python3
"""
recursive function the queries reddit api and
returns a list containing titles of hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], next=""):
    base_url = "https://api.reddit.com/r/{}/hot?after={}".format(
        subreddit, next)
    req_headers = {"user-agent": " Apple-safari"}
    try:
        data = requests.get(base_url, headers=req_headers,
                            allow_redirects=False).json()
        hot_posts = data['data']['children']
        for posts in hot_posts:
            hot_list.append(posts['data']['title'])
        next = data['data']['after']
        if next:
            recurse(subreddit, hot_list, next)
        return (None)

    except Exception:
        return (None)
