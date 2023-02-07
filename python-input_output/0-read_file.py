#!/usr/bin/python3
def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, "r" ,encoding= "UTF8") as myfile:
        for i in myfile:
            print(i.strip())
