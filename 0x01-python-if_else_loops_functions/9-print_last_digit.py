#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    ld = num % 10
    print("{}".format(ld), end="")
    return ld
