#!/usr/bin/python3

import requests
import json

def top_ten(subreddit) -> None:
    """ prints the titles of the first 10 hot posts listed for a given subreddit.
        Args:
            subreddit: str - the subredit to get the top 10 0f
        Returns:
            None
    """
    limit: int = 10
    url: str = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit={limit}"
    headers: dict = {
        'User-Agent': 'My User Agent 1.0',
    }
    try:
        response = requests.get(url=url, headers=headers, allow_redirects=False)
        data: dict = json.loads(response.text)["data"]["children"]
        for obj in data:
            print(obj["data"]["title"])
    except Exception:
        print("None")
