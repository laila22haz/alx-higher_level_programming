#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv) - 1
    if (arg == 1):
        print("{} argument:".format(arg))
    elif (arg == 0):
        print("{} arguments.".format(arg))
    else:
        print("{} arguments :".format(arg))
    for i in range(arg):
        print("{}: {}".format(i+1, argv[i+1]))
