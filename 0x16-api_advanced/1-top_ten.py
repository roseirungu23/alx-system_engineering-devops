#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10 hot posts """

import requests

def top_ten(subreddit):
    """Reddit API endpoint for getting hot posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
     
        response = requests.get(url, headers=headers)

        
        if response.status_code == 200:
        
            data = response.json()
            posts = data['data']['children'][:10]

            if not posts:
                print(f"No hot posts found for subreddit: {subreddit}")
                return

            for post in posts:
                title = post['data']['title']
                print(f"- {title}")

        elif response.status_code == 404:
            print("None")
        else:
            print(f"Error: {response.status_code}")
            print("None")

    except Exception as e:
        print(f"Exception: {e}")
        print("None")
