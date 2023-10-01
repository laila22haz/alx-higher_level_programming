#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email' : email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(repr) as response:
        page = response.read()
