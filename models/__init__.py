#!/usr/bin/python3
"""Initialize app storage type """
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# create a unique instance for either DBStorage or FileStorage
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data into memory buffer
storage.reload()
