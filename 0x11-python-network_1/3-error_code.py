#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
