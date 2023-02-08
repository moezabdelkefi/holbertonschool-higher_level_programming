#!/usr/bin/python3
"""define a function write_file"""


def write_file(filename="", text=""):
    """ return length of the text"""
    with open(filename, "w", encoding="UTF8") as myfile:
        myfile.write(text)
        return len(text)
