#!/usr/bin/python3

"""
Main command line interface
"""


import cmd
from typing import Any
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class to take care of command stuff
    """

    intro = "Welcome to HBNB-MACRODAT command prompt."
    prompt = "(hbnb) "

    def cmdloop(self, intro: Any | None = None) -> None:
        """loop function"""
        return super().cmdloop(intro)

    def do_quit(self, obj):
        """quit"""
        return self.do_EOF(obj)


    def do_EOF(self, obj):
        """quit"""
        print("Exiting.")
        return True

    def do_create(self, arg):
        """creates a class instance"""
        if not arg:
            print("** class name missing **")
            return
        if arg == "BaseClass":
            b = BaseModel()
            storage.save()
            print(b.id)
        else:
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
