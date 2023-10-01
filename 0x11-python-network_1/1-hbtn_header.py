#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

import urllib.request
import sys

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        data = response.read()
        headers = response.headers["X-Request-Id"]
        print(headers)
