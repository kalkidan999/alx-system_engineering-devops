#!/usr/bin/python3
"""
function that queries Reddit API and returns
number of subscribers (not active users, total subscribers)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers={"User-Agent": "kalkidan"})
    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
