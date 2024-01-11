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
        if arg == "BaseModel":
            b = BaseModel()
            storage.save()
            print(b.id)
        else:
            print("** class doesn't exist **")
            return

    def help_create(self):
        """ help for create """
        print(
            """Creates a class. Example usage:
create BaseModel
Returns id."""
            )

    def do_show(self, arg):
        """show"""
        if not arg:
            print("** class name missing **")
            return
        args = str(arg).split(' ')
        if args[0] == "BaseModel":
            if len(args) < 2:
                print("** instance id missing **")
                return
            id_ = "BaseModel." + args[1]
            if id_ not in storage.all():
                print("** no instance found **")
                return
            storage.all().get(id_).__str__()
        else:
            print("** class doesn't exist **")
            return

    def help_show(self):
        """ help for show """
        print(
            """show: Prints the string representation of an instance
based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing **
(ex: $ show)
If the class name doesn’t exist,
print ** class doesn't exist ** (ex: $ show MyModel)
If the id is missing, print **
instance id missing ** (ex: $ show BaseModel)
If the instance of the class name doesn’t exist
for the id, print ** no instance found **
(ex: $ show BaseModel 121212)"""
            )

    def do_destroy(self, arg):
        """destroy"""
        if not arg:
            print("** class name missing **")
            return
        args = str(arg).split(' ')
        if args[0] == "BaseModel":
            if len(args) < 2:
                print("** instance id missing **")
                return
            id_ = "BaseModel." + args[1]
            if id_ not in storage.all():
                print("** no instance found **")
                return
            storage.all().pop(id_)
            storage.save()
        else:
            print("** class doesn't exist **")
            return

    def help_destroy(self):
        """ help for destory """
        print(
            """destroy: Deletes an instance based on the class name and id
(save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
If the class name is missing, print ** class name missing ** (ex: $ destroy)
If the class name doesn’t exist,
print ** class doesn'texist ** (ex:$ destroy MyModel)
If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
If the instance of the class name doesn’t exist for
the id, print ** no instance found **
(ex: $ destroy BaseModel 121212)"""
            )

    def do_all(self, arg):
        """All"""
        if not arg:
            print([v.toStr() for k, v in storage.all().items()])
            return
        args = str(arg).split(' ')
        if args[0] == "BaseModel":
            print([v.toStr() for k, v in storage.all().items()
                   if str(k).startswith("BaseModel")])
        else:
            print("** class doesn't exist **")
            return

    def help_all(self):
        """ help for all """
        print(
            """all: Prints all string representation of all instances
based or not on the class name. Ex: $ all BaseModel or $ all.
The printed result must be a list of strings (like the example below)
If the class name doesn’t exist, print
** class doesn't exist ** (ex: $ all MyModel)"""
            )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
