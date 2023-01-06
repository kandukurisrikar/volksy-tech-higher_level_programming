#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    for i in matrix:
        s = map(lambda num: num**2, i)
        lst.append(list(s))
    return lst
