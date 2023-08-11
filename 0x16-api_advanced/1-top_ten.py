#!/usr/bin/python3
"""prints the titles of the first 10 hot"""

import json
import requests


def top_ten(subreddit) -> None:
    """ prints the titles of the first 10 hot posts for a given subreddit.
        Args:
            subreddit: str - the subredit to get the top 10 0f
        Returns:
            None
    """
    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit={limit}"
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    try:
        response = requests.get(
                    url=url,
                    headers=headers,
                    allow_redirects=False
                )
        data = json.loads(response.text)["data"]["children"]
        for obj in data:
            print(obj["data"]["title"])
    except Exception:
        print("None")
