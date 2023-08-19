#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = {}
    for k, v in a_dictionary.items():
        v = v * 2
        n_dict.update({k: v})
    return n_dict
