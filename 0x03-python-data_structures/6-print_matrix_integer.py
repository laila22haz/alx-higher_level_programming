#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for colomn in range(len(matrix[row])):
            if colomn != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][colomn]), end='')
        print()