#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())

    for k in list_key:
        if value == a_dictionary.get(k):
            del a_dictionary[k]
    return a_dictionary
