#!/bin/bash
# cURL body size
read -p url
send=$(curl "$url")
response=$(curl -s -w "%{size_download}" "$url")
size=$(curl -sI "$url" | grep -iF 'content-length')
echo "$response"
echo "$size"
