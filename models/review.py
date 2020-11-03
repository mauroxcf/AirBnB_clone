#!/usr/bin/python3
"""this module contains the review CLass for the project Airbnb_clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that contains certain info """
    place_id = ""
    user_id = ""
    text = ""
