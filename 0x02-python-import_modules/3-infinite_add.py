#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = len(argv) - 1
    sum = 0
    for i in range(arg):
        sum += int(argv[i+1])
    print("{}".format(sum))
