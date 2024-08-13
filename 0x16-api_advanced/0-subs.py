#!/usr/bin/python3
"""query number of subscriber in a reddit"""

"""importing request to make http request to a server"""
import requests

def number_of_subscribers(subreddit):
    """number_of_subscribers() function returns number of subscribers on reddit"""
    if subreddit is None or type(subreddit) is not str:
       return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
      "User-Agent": "windows11:0X16.api.advanced/1.0 (by /u/natishget_33)"
    }
    try:
       req = requests.get(url, headers=headers, allow_redirects=False)
       if req.status_code == 400:
          return 0
       result = req.json().get("data")
       return result.get("subscribers")
    except (Exception):
       print('Not Found')
       return (0)
      
