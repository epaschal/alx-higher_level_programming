#!/usr/bin/python3
for i in range(0,10):
    for j in range(0,10):
        if i != 9 or j != 9:
            print("{}{}, ".format(i, j), end="")
print("99")