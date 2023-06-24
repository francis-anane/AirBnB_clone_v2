#!/usr/bin/python3
"""This is the base model class for AirBnB"""

from sqlalchemy.orm import declarative_base
import uuid
from models import storage
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """defines all common attributes/methods for the AirBnB_clone objects
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel
        Args:
            args: tuple of arguments to Basemodel to create a new object
            kwargs: key/value arguments to Basemodel to create a new object
        Attributes:
            id: Unique identity for objects
            created_at: The time an object was created
            updated_at: The time an object was updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the class instace"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return string representation"""
        return self.__str__()

    def save(self):
        """Save object updates"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dictionary representation of object"""
        obj_dict = {}  # holds dictionary representation of object
        obj_dict.update(self.__dict__)
        # convert datetime objects to string string (created_at and updated_at)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        # add object's class name to dictionary
        obj_dict.update({"__class__": type(self).__name__})
        if "_sa_instance_state" in obj_dict.keys():
            del obj_dict["_sa_instance_state"]
        return obj_dict

    def delete(self):
        """ delete object
        """
        storage.delete(self)
