#!/usr/bin/python3
"""this module contains the Base CLass for the project Airbnb_clone
"""


import uuid
import datetime
import models


dati = datetime.datetime


class BaseModel():
    """
    Base class for all class in airbnb_clone project
    """
    def __init__(self, *args, **kwargs):
        """Constructor - initialization of new or existing instances

        Args:
            args (list): nothing
            kwargs (dict): one dict to create an object
        """
        if kwargs:
            new_dict = kwargs["data"]
            for k, v in new_dict.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        val = dati.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                        self.__dict__[k] = val
                    else:
                        self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dati.now()
            self.updated_at = dati.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string with this format [<class name>] (<self.id>) <self.__dict__>

        Returns:
            str: format - [<class name>] (<self.id>) <self.__dict__>
        """
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """updates the update_at atrribute
        """
        self.updated_at = dati.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict with all values of __dict__
            adds a new key('__class__') with the self class name
            converts created_at and updated_at to str in ISO format

        Returns:
            dict: new_dict
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
