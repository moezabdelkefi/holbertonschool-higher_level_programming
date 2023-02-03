#!/usr/bin/python3

"""define a function that print My name is <first name> <last name> """

"""
raises:
    TypeError: first_name must be a string
    TypeError: last_name must be a string
    

"""

def say_my_name(first_name, last_name=""):

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name)!= str:
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))
