#!/usr/bin/python3
"""
Este modulo tiene un programa.
"""
import cmd
from shlex import split
import models
from models.base_model import BaseModel

clases = {"BaseModel": BaseModel}


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

    def do_create(self, arg):
        """Crea una  instancia"""
        if not arg:
            print("** class name missing **")
            return

        if arg in clases:
            valor = clases[arg]
            instancia = valor()
            print(instancia.id)
            instancia.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        args = split(args)

        if not args:
            print("** class name missing **")
            return

        if args[0] in clases:
            if len(args) == 1:
                print("** instance id missing **")
                return

            key = "{}.{}".format(args[0], args[1])

            if key in models.storage.all():
                    print(models.storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        args = split(args)

        if not args:
            print("** class name missing **")
            return

        if args[0] in clases:
            if len(args) == 1:
                print("** instance id missing **")
                return
            
            key = "{}.{}".format(args[0], args[1])

            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        arg = split(arg)
        lista = []

        if len(arg) == 0:
            for valor in models.storage.all().values():
                lista.append(str(valor))
                print(lista)
                return

        if arg[0] in clases:
            for clave in models.storage.all():
                if arg[0] in clave:
                    lista.append(str(models.storage.all()[clave]))
            print(lista)
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        args = split(args)

        if len(args) == 0:
            print("** class name missing **")
            return
        
        if args[0] in clases:
            if len(args) >= 2:
                key = "{}.{}".format(args[0], args[1])
                if key in models.storage.all():
                    if len(args) >= 3:
                        valor_dic = models.storage.all()[key]
                        if hasattr(valor_dic, args[2]):
                            if len(args) >= 4:
                                setattr(valor_dic, args[2], args[3])
                                models.storage.save()
                            else:
                                print("** value missing **")
                        else:
                            if len(args) >= 4:
                                setattr(valor_dic, args[2], args[3])
                                models.storage.save()
                            else:
                                print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
