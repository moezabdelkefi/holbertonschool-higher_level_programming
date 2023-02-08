#!/usr/bin/python3
""""define a function appen_write"""


def append_write(filename="", text=""):
    """append a new string"""

    with open(filename, 'a', encoding= 'utf8') as f:
        f.write(text)
        return len(text)
