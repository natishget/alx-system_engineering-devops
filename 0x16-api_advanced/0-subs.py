#!/usr/bin/python3

"""Query the number of subscribers in a Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given Reddit subreddit."""
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "windows11:0X16.api.advanced/1.0 (by /u/natishget_33)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 400:
            return 0
        result = response.json().get("data", {})
        return result.get("subscribers", 0)
    except requests.exceptions.RequestException:
        print('Request failed')
        return 0
