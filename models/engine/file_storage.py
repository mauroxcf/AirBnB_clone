#!/usr/bin/python3
"""This module cintains the FileStorage class
"""


import json
import datetime
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    def __init__(self):
        """ constructor """
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
        """ try:
            with open(__file_path) as fl:
                json_str = fl.read()
                if json_str != '':
                    temp_obj = json.loads(json_str)
        except FileNotFoundError:
            with open(__file_path, "w") as fl:
                pass """
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
        """if __file_path: """
        #se debe modificar el bloque de codigo para poder implementarlo con User, mirar linea 64
        try:
            with open(self.__file_path, "r") as file1:
                """ str_file = str(file1.read()) """
                temp = json.load(file1)

                for key in temp.keys():
                    new_instance = BaseModel(data=temp[key])
                    self.__objects[key] = new_instance
        except FileNotFoundError:
            pass
