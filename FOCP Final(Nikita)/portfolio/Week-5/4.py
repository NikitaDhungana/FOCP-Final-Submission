'''
Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.
'''

import requests
url = "https://www..com.np"  
try:
    response = requests.get(url, timeout=5)  
    if response.status_code == 200:
        print(f"The website at {url} is working (HTTP {response.status_code}).")
    else:
        print(f"The website at {url} is reachable but returned HTTP {response.status_code}.")
except requests.exceptions.RequestException as e:
    print(f"Failed to reach the website at {url}. Error: {e}")
