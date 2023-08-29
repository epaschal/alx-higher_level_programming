#!/usr/bin/python3
"""A class that defines a square
"""
class Square:
    """A class that describes a square by its size
    """
    def __init__(self, size=0):
        """A methos to initialize the object
        Args:
            size (int): size is an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """A method to find the area of the object
        """
        a = self.__size ** 2
        return a
    @property
    def size(self):
        """A method to retrieve the size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """A method to set the value of size
        Args:
            value (int): The new value to be set as the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def my_print(self):
        """A method to print a square using #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range (self.__size):
                    print("#", end="")
                print()
