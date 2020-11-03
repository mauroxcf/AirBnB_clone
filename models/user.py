#!/usr/bin/python3
"""this module contains the User CLass for the project Airbnb_clone
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ User class that contains certain info """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
