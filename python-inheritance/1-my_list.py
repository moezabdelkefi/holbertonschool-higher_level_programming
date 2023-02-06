#!/usr/bin/python3
""" define a class MyList  """


class MyList(list):
    """ inherits from list"""

    def print_sorted(self):
        print(sorted(self))
