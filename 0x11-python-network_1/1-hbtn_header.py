#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        request_id = response.headers["X-Request-Id"]
        print(request_id)
