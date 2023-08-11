#!/usr/bin/python3
"""Gets the number of subscribers"""
import requests
import json


def number_of_subscribers(subreddit: str) -> int:
    """ Gets the number of subscribers in a given subreddit
        Args:
            subreddit: str - The subreddit to query for
        Returns:
            The number of subscribers or 0 if the subreddit doesn't exist.
    """
    headers: dict = {
        'User-Agent': 'My User Agent 1.0',
    }
    url: str = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(
                    url=url,
                    headers=headers,
                    allow_redirects=False
                )
        data: dict = json.loads(response.text)
        return data["data"]["subscribers"]
    except Exception:
        return 0
