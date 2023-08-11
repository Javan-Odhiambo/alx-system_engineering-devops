#!/usr/bin/python3

import requests
import json

def recurse(subreddit, hot_list=[], after=25) -> list:
    """ prints the titles of the first 10 hot posts listed for a given subreddit.
        Args:
            subreddit: str - the subredit to get the top 10 0f
        Returns:
            None
    """
    headers: dict = {
        'User-Agent': 'My User Agent 1.0',
    }
    url: str = f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}"
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.json().get("error", 200) == 404:
        return None
    
    if not after:
        return hot_list
            
    data: dict = json.loads(response.text)["data"]["children"]
    after: str = json.loads(response.text)["data"]["after"]
    for obj in data:
        hot_list.append(obj.get("title"))
    return recurse(subreddit, hot_list, after)

        

   
