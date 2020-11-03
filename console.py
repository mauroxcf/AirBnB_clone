#!/usr/bin/python3
""" Command Interpreter """


import cmd
import sys
import models

BaseModel = models.base_model.BaseModel
User = models.user.User
State = models.state.State
City = models.city.City
Amenity = models.amenity.Amenity
Place = models.place.Place
Review = models.review.Review

dict_class = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


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

    if args[0] in dict_class:
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

    def do_EOF(self, arg):
        """ if there is a End of File,
        quit the command interpreter """
        return True

    def do_create(self, arg):
        """ create a instance """
        if arg in dict_class:
            cls_name = dict_class[arg]
            new_inst = cls_name()
            new_inst.save()
            print(new_inst.id)
            return

        if arg == "":
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

        if args[0] in dict_class:
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

        if arg == "" or args[0] in dict_class:
            all_inst = models.storage.all()
            list_str = []

            for key, val in all_inst.items():
                if arg in key:
                    list_str.append(val.__str__())
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

            if '"' in args[3]:
                i = 3
                concat = args[3].replace('"', "")
                i += 1
                while i < len(args):
                    if '"' in args[i]:
                        concat += " " + args[i].replace('"', "")
                        break
                    concat += " " + args[i]
                    i += 1
                if '"' in concat:
                    args[3] = concat.replace('"', "")
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

    def help_create(self):
        """ help create command """
        print("Creates a object, saves it to the JSON file and prints the id")

    def help_show(self):
        """help show command """
        print("Prints representation of an object based on the name and id")

    def help_destroy(self):
        """help destroy command """
        print("Deletes an object based on the name and id")

    def help_all(self):
        """help all command """
        print("prints all objects")

    def help_update(self):
        """ help update command """
        txt = "updating the attribute"
        print("updates the object by name and id adding or", txt)

    def help_EOF(self):
        """ help EOF command """
        print("EOF exit the program\n")

    def emptyline(self):
        """ do nothing """
        pass

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()
