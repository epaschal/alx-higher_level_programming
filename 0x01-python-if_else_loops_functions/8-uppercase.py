#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            num = 32
        else:
            num = 0
        print("{}".format(chr(ord(i) - num)), end="")
    print()
