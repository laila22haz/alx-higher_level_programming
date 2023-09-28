#!/bin/bash
# cURL to the end
curl -LI "$1" -w '%{http_code}' -s
