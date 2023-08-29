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
            raise TypeError("size must be a integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
