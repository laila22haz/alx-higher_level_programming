#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error cod: {}".format(e.code))
