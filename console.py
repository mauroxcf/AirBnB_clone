#!/usr/bin/python3
""" Command Interpreter """


import cmd
import sys
import models

baseModel = models.base_model.BaseModel
userinst = models.user.User # nueva adiccion por la clase user

def errors(err):
    if err == "!cl_name":
        print("** class name missing **")
    elif err == "!cls_exist":
        print("** class doesn't exist **")
    elif err == "!id":
        print("** instance id missing **")
    elif err == "!found":
        print("** no instance found **")
    elif err == "!att_name":
        print("** attribute name missing **")
    elif err == "!value":
        print("** value missing **")


def getobj(arg):
    """returns an instance by the key

    Args:
        arg (str): the commands arguments

    Returns:
        obj: the object if is found
    """
    args = arg.split()

    if arg == "":
        errors("!cl_name")
        return 0

    #nueva adicion por la clase User
    if args[0] == "BaseModel" or args[0] == "User":
        if len(args) < 2:
            errors("!id")
            return 0
        instances = models.storage.all()

        key = args[0] + "." + args[1]
        if key in instances:
            return instances[key]
        else:
            errors("!found")
    else:
        errors("!cls_exist")
    return 0


class HBNBCommand(cmd.Cmd):
    """ commands """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit the command interpreter """
        return True

    def do_create(self, arg):
        """ create a instance of Basemodel """
        if arg == "BaseModel":
            new_inst = baseModel()
            new_inst.save()
            print(new_inst.id)

        #nueva adiccion por el modulo user
        if arg == "User":
            new_inst = userinst()
            new_inst.save()
            print(new_inst.id)

        elif arg == "":
            errors("!cl_name")
        else:
            errors("!cls_exist")

    def do_show(self, arg):
        """prints the string representation of an instance

        Args:
            arg (str): class class and instance id
        """
        my_inst = getobj(arg)
        if my_inst:
            print(my_inst)

    def do_destroy(self, arg):
        """deletes an instance by the class name and id

        Args:
            arg (str): class class and instance id
        """

        args = arg.split()

        if arg == "":
            errors("!cl_name")
            return

        # nueva adiccion en la linea 108 por la clase User
        if args[0] == "BaseModel" or args[0] == "User":
            if len(args) < 2:
                errors("!id")
                return

            key = args[0] + "." + args[1]
            all_obj = models.storage.all()
            if key in all_obj:
                temporal = all_obj[key]
                all_obj.pop(key)
                models.storage.save()
                del temporal
            else:
                errors("!found")
        else:
            errors("!cls_exist")

    def do_all(self, arg):
        """prints all string representation of all instances

        Args:
            arg (str): class name
        """
        args = arg.split()

        # nueva adicion por la clase User en la linea 134
        if arg == "" or arg == "BaseModel" or arg == "User":
            all_inst = models.storage.all()
            list_str = []
            for i in all_inst.values():
                list_str.append(i.__str__())
            print(list_str)
        else:
            errors("!cls_exist")

    def do_update(self, arg):
        """updates an instance by class name and id adding or updating
        the attribute

        Args:
            arg (str): class name, instance id and attributes
        """
        args = arg.split()

        my_inst = getobj(arg)

        if my_inst:
            if len(args) < 3:
                errors("!att_name")
                return
            if len(args) < 4:
                errors("!value")
                return

            if args[2] in ("created_at", "updated_at", "id"):
                return

            if args[3][0] == '"':
                i = 3
                concat = args[3][1:]
                i += 1
                while i < len(args):
                    if '"' in args[i]:
                        concat += " " + args[i][:-1]
                        break
                    concat += " " + args[i]
                    i += 1
                if concat[-1] == '"':
                    args[3] = concat[:-1]
                else:
                    args[3] = concat

            try:
                convert = int(args[3])
            except ValueError:
                try:
                    convert = float(args[3])
                except ValueError:
                    convert = args[3]

            my_inst.__dict__[args[2]] = convert
            my_inst.save()

    def help_quit(self):
        """ help quit command """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """ do nothing """
        pass

    do_EOF = do_quit
    help_EOF = help_quit
    # si hay un error con los checkers, crear el metodo do_EOF y help_EOF

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
