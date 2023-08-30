#!/usr/bin/python3
"""A class that defines a square
"""
class Square:
    """A class that describes a square by its size and position in space
    """
    def __init__(self, size=0, position=(0, 0)):
        """A methos to initialize the object
        Args:
            size (int): size is an integer
            position (tuple): position of square
        """
        self.__size = size
        self.__position = position
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
    @property
    def position(self):
        """A method to retrieve the position
        """
        return self.__position
    @position.setter
    def position(self, value):
        """A method that sets the value of position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def my_print(self):
        """A method to print a square using #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range (self.__size):
                    print("#", end="")
                print()

