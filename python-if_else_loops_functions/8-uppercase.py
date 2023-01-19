#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            new_string += chr(ord(char) - ord('a') + ord('A')) + ''
        else:
            new_string += char + ''
    print(new_string)
    print()
