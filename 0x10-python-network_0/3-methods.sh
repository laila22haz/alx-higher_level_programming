#!/bin/bash
# cURL Method
curl -sL "$1" | grep "Allow" | cut -d " " -f 2-
