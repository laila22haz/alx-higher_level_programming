#!/bin/bash
# cURL a JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
