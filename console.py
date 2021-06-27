#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Holberton AirBnB clone console
    contains the entry point of the command interpreter
    quit and EOF to exit the program
    help dispays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = '(hbnb) '
    intro = 'command line interpreter for HBnB, for more info type help'

    def do_EOF(self, line):
        """Exits on EOF"""
        return True

    def do_quit(self, line):
        """exits when typing quit"""
        return True

    def emptyline(line):
        """passing emptyline do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
