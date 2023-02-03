#!/usr/bin/python3

"""define a function that prints a
text with 2 new lines after each of these characters """


def text_indentation(text):

    """
    a function that prints a text with 2 new lines
    after each of these characters
    typeError: text must be a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    characters = [".", "?", ":"]
    for character in characters:
        text = text.replace(character, character + "\n\n")
    print(text.strip(), end="")
