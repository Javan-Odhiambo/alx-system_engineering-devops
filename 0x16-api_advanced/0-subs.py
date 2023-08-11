#!/usr/bin/python3
"""Gets the number of subscribers"""
import json
import requests


def number_of_subscribers(subreddit: str) -> int:
    """ Gets the number of subscribers in a given subreddit
        Args:
            subreddit: str - The subreddit to query for
        Returns:
            The number of subscribers or 0 if the subreddit doesn't exist.
    """
    header = {
        'User-Agent': 'My User Agent 1.0',
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(
                    url=url,
                    headers=headers,
                    allow_redirects=False
                )
        dat = json.loads(response.text)
        return data["data"]["subscribers"]
    except Exception:
        return 0
