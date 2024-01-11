#!/usr/bin/python3

"""
Main command line interface
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    class to take care of command stuff
    """

    intro = "Welcome to HBNB-MACRODAT command prompt."
    prompt = "(hbnb)"


    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
