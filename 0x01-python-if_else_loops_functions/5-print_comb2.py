#!/usr/bin/python3
for letter in range(0, 100):
    if letter == 99:
        print("{} ".format(letter))
    else:
        print("{:02}".format(letter), end=', ')
