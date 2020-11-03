#!/usr/bin/python3
"""this module contains the City CLass for the project Airbnb_clone
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that contains certain info """
    state_id = ""
    name = ""
