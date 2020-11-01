#!/usr/bin/python3
"""this module contains the unittesting for BaseModel class
"""


import unittest
import json
import pep8
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    """ def test__(self):
        pass """
