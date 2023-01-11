#!/usr/bin/python3
"""class"""


class Square:
    ''' square size'''
    def __init__(self, size=0):
        """Constructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        square.__size = size

    def area(self):
        """Area of square"""
        return (square._size * square._size)
