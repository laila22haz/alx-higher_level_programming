#!/usr/bin/python3
'''
JSON representation
'''
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try:
    exist_file = load_from_json_file(filename)
except FileExistsError:
    exist_file = []

save_to_json_file(exist_file + sys.argv[1:], filename)
