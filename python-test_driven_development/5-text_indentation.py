#!/usr/bin/python3
"""define a function that prints a 
text with 2 new lines after each of these characters """

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(new_text.strip(), end="")
