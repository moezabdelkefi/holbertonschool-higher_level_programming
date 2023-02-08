#!/usr/bin/python3
"""this is the declaration of the module"""


def write_file(filename="", text=""):
    """this Module open the file and write in it"""
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
    f.close()
    return len(text)
