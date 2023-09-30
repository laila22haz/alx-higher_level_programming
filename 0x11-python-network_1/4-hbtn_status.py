#!/usr/bin/python3
"""What's my status? #1
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    data = res.text
    resType = type(data)
    print(f"Body response:\n\t- type: {resType}\n\t\
- content: {data}")
