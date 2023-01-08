#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    li = a_dictionary
    for i in range(len(li)):
        if li[i] == key:
            li[i] = value
    return (a_dictionary)
