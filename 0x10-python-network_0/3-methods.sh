#!/bin/bash
# cURL Method
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
