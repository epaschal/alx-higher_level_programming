#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == None:
        return 0
    num = 0
    den = 0
    for t in my_list:
        num += t[0] * t[1]
        den += t[1]
    return num/den
