#!/usr/bin/python3
"""0. What's my status? #0
"""

import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        the_page = response.read()

