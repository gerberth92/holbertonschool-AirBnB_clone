#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()