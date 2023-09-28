#!/bin/bash
# cURL to the end
curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s
