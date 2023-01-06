#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for coloumn in row:
                print('{:d}'.format(coloumn), end=''
                      if coloumn != row[-1] else '\n')
