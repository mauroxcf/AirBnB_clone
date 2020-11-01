#!/usr/bin/python3
""" Command Interpreter """


import cmd, sys

class HBNBCommand(cmd.Cmd):
    """ commands """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit the command interpreter """
        return True

    def help_quit(self):
        """ help quit command """
        print("Quit command to exit the program")

    def emptyline(self):
        """ do nothing """
        pass

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
