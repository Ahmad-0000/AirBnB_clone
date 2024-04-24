#!/usr/bin/python3
"""Command interpreter module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class to manipulte the "storage engine" """

    prompt = "(hbnb) "

    def emptyline(self):
        """Overidden "emptyline" method"""

        pass

    def do_quit(self, arg):
        """Quitting the interpreter"""

        return 1

    def do_EOF(self, arg):
        """Quitting the interpreter"""

        print()
        return 1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
