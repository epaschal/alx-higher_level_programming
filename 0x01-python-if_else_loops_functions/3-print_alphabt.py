#!/usr/bin/python3
i = 97
while i <= 122:
    if (i == ord("e")) or (i == ord("q")):
        continue
    print("{}".format(chr(i)), end="")
    i += 1
