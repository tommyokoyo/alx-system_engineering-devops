#!/usr/bin/python3

"""
This scripts fetches Number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries for number of subscribers
    """
    req_headers = {"user-agent": " Apple-safari"}
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        data = requests.get(base_url, headers=req_headers).json()
        number_of_subscribers = data["data"]["subscribers"]
        return number_of_subscribers

    except Exception:
        return 0
