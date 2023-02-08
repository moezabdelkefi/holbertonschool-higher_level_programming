#!/usr/bin/python3
"""define a function write_file"""


def write_file(filename="", text=""):
    """ return length of the text"""
    with open(filename, "r", encoding="UTF8") as myfile:
        return len(text)
