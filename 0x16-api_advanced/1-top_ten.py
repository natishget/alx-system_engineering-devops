#!/usr/bin/python3

"""
queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    prints the titles of the first 10 hot posts listed for
    a given subreddit
    """
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{subreddit}?sort=hot&limit=10"
    headers = {
        "User-Agent": "windows11:0X16.api.advanced/1.0 (by /u/natishget_33)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 400:
            return 0
        result = response.json().get("data", {})
        return result.get("subscribers", 0)
    except requests.exceptions.RequestException:
        print('Request failed')
        return 0
