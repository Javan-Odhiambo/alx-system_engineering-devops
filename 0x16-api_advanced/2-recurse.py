#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit.
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=25) -> list:
    """returns a list containing the titles of all hot articles
        for a given subreddit.
        Args:
            subreddit: str - the subredit to get the top 10 0f
        Returns:
            None
    """
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.json().get("error", 200) == 404:
        return None

    if not after:
        return hot_list

    data = json.loads(response.text)["data"]["children"]
    after = json.loads(response.text)["data"]["after"]
    for obj in data:
        hot_list.append(obj.get("title"))
    return recurse(subreddit, hot_list, after)
