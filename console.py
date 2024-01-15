#!/usr/bin/python3

"""
Main command line interface
documentation:
Write a program called console.py that contains
the entry point of the command interpreter:
You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
"""


import cmd
import re
from models import storage
""" 6. Console 0.0.1 """


class HBNBCommand(cmd.Cmd):
    """
    class to take care of command stuff
    """

    intro = "Welcome to HBNB-MACRODAT command prompt."
    prompt = "(hbnb) "

    def precmd(self, line: str) -> str:
        """ pre-command checks """
        if not line:
            return '\n'
        pattern = re.compile(r"(\w+)\.(\w+)\(([^)]*)\)")
        match_ = pattern.findall(line)
        if not match_:
            return super().precmd(line)
        match_ = match_[0]
        if match_[1] == "all":
            # print all
            if match_[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            objs = storage.classes()[match_[0]].all()
            objs = [o.__str__() for o in objs]
            print(objs)
            return ""
        elif match_[1] == "count":
            if match_[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            objs = storage.classes()[match_[0]].all()
            print(len(objs))
            return ""
        elif match_[1] in ["show", "destroy", "update"]:
            if match_[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(match_) < 3:
                print("** instance id missing **")
                return
            third = ' '.join([e.strip() for e in match_[2].split(',')])
            return ' '.join([match_[1], match_[0], third])

    def onecmd(self, line: str) -> bool:
        """ one cmd """
        if not line:
            return
        return super().onecmd(line)

    def do_quit(self, obj):
        """quit"""
        quit()

    def emptyline(self) -> bool:
        """override"""
        return False

    def do_EOF(self, obj):
        """quit"""
        quit()

    def do_create(self, arg):
        """creates a class instance"""
        if not arg:
            print("** class name missing **")
            return
        if arg in storage.classes():
            b = storage.classes()[arg]()
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
        if args[0] in storage.classes():
            if len(args) < 2:
                print("** instance id missing **")
                return
            id_ = args[0] + "." + args[1]
            if id_ not in storage.all():
                print("** no instance found **")
                return
            print(storage.all().get(id_).__str__())
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
        if args[0] in storage.classes():
            if len(args) < 2:
                print("** instance id missing **")
                return
            id_ = args[0] + "." + args[1]
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

    def do_update(self, arg):
        """update"""
        if not arg:
            print("** class name missing **")
            return

        def nnTuple(t: tuple):
            if t[0]:
                return t[0]
            return t[1]

        def cast_to_appropriate_type(obj):
            """casts"""
            if str(obj).startswith('"') and str(obj).endswith('"'):
                return str(obj[1:-1])
            if '.' in obj:
                return float(obj)
            if str(obj).isdigit():
                return int(obj)
            return str(obj)
        pattern = re.compile(r'\b(\w+)|"([^"]+)"')
        matches = pattern.findall(arg)
        args = [nnTuple(e) for e in matches]
        if args[0] in storage.classes():
            if len(args) < 2:
                print("** instance id missing **")
                return
            id_ = args[0] + "." + args[1]
            if id_ not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all().get(id_),
                    str(cast_to_appropriate_type(args[2])),
                    cast_to_appropriate_type(args[3])
                    )
            storage.save()
        else:
            print("** class doesn't exist **")
            return

    def help_update(self):
        """ help for update """
        print(
            """update: Updates an instance based on the class name and id
by adding or updating attribute (save the change into the JSON file).
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
Only one attribute can be updated at the time
You can assume the attribute name is valid (exists for this model)
The attribute value must be casted to the attribute type
If the class name is missing,
print ** class name missing ** (ex: $ update)
If the class name doesn’t exist,
print ** class doesn't exist ** (ex: $ update MyModel)
If the id is missing,
print ** instance id missing ** (ex: $ update BaseModel)
If the instance of the class name doesn’t exist for the id,
print ** no instance found ** (ex: $ update BaseModel 121212)
If the attribute name is missing, print ** attribute
name missing ** (ex: $ update BaseModel existing-id)
If the value for the attribute name doesn’t exist,
print ** value missing **
(ex: $ update BaseModel existing-id first_name)
All other arguments should not be used
(Ex: $ update BaseModel 1234-1234-1234 email
"aibnb@mail.com" first_name "Betty"
=
$ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
id, created_at and updated_at cant’ be updated.
Only “simple” arguments can be updated: string, integer and float."""
            )

    def do_all(self, arg):
        """All"""
        if not arg:
            print([v.toStr() for k, v in storage.all().items()])
            return
        args = str(arg).split(' ')
        if args[0] in storage.classes():
            print([v.toStr() for k, v in storage.all().items()
                   if type(v).__name__ == args[0]])
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
