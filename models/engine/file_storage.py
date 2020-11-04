#!/usr/bin/python3
"""This module cintains the FileStorage class
"""


import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class_names = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage():
    """ Class FileStorage """

    def __init__(self):
        """ Constructor - initialization of instances"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects

        Returns:
            dict: dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """adds a new objects in __objects

        Args:
            obj (obj): one objects
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """saves the serialization of __objects in one file.json
        """
        with open(self.__file_path, "w") as fl:
            if not self.__objects:
                fl.write("{}")
            else:
                temp_dict = {}
                for key1 in self.__objects.keys():
                    temp_dict[key1] = self.__objects[key1].to_dict()
                fl.write(json.dumps(temp_dict))

    def reload(self):
        """ deserializes the JSON file to """
        try:
            with open(self.__file_path, "r") as file1:
                """ str_file = str(file1.read()) """
                temp = json.load(file1)

                for key in temp.keys():
                    for key_cls in class_names.keys():
                        if key_cls in key:
                            name_cls = class_names[key_cls]
                            new_instance = name_cls(**temp)
                            self.__objects[key] = new_instance
                            break
        except FileNotFoundError:
            pass
