#!/usr/bin/python3
"""init file for models
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
