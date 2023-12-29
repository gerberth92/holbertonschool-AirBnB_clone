#!/usr/bin/python3
"""
Este modulo tiene un programa.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Esta clase define un programa llamado "hbnb".
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return (True)
    
    def do_EOF(self, args):
        """EOF command to exit the program"""
        return (True)
    
    def do_help(self, args):
        """Documented commands (type help <topic>):"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
