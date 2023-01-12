#!/usr/bin/python3
"""strng"""

class Square:
    """class square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def area(self):
            a = self.__size * self.__size
            return a

        def my_print(self):
            if self.__size == 0:
                print("")
            for i in range(0, self._size):
                for j i range(0, self._size):
                    print("#" ,end="")
                print()
