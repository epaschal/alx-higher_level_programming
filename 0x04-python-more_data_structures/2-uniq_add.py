#!/usr/bin/python3
def uniq_add(my_list=[]):
    s_list = set(my_list)
    num = 0
    for i in s_list:
        num += i
    return num
