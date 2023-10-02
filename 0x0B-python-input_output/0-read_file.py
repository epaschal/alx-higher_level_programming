#!/usr/bin/python3
""" Module that contains a function that reads a text file
"""

def read_file(filename=""):
    """ Function that reads a text file

    Args:
        filename: filename

    Raises:
        Exception: if file not found
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
