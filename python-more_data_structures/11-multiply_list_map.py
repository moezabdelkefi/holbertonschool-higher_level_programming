#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    result = list(map(lambda item: item * number, my_list))
    return result
