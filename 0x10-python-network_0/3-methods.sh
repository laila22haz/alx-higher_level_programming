#!/bin/bash
# cURL Method
curl -sL "$1" | grep -i "Allow" | cut -d ':' -f 2-
