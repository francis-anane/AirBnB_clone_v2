#!/usr/bin/python3

"""file_storage module"""

import datetime
import json


class FileStorage:
    """ serializes objects to a JSON file and deserializes JSON file to objects

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Stores all objects by class_name.id in a dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""

        dic = {}
        if cls:
            objs_dict = self.__objects
            for key in objs_dict:
                class_name = key.replace('.', ' ')
                class_name = class_name.split()
                if (class_name[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to __objects by using <class name>.<id> as key
        Args:
            obj:  Instance of a class
        """
        if obj:
            self.__objects.update(
                {f"{type(obj).__name__}.{obj.id}": obj})

    def save(self):
        """ Serializes __objectts to the JSON file __file_path"""

        try:
            # reassign to include updated key/values of attributes
            # in the JSON file
            self.__objects[f"{type(self).__name__}.{self.id}"] = self

        except AttributeError:
            pass  # for now

        with open(self.__file_path, "w", encoding="utf-8") as a_file:

            # get objects dictionary with dictionary complexsion
            objs_dict = {}

            objs_dict.update({key: self.__objects[key].to_dict(
            ) for key in self.__objects})

            # serialize objects to JSON
            json.dump(objs_dict, a_file)

    def classes(self):
        """Returns a dictionary mapping class names to the class
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes the JSON file __file_path to __objects"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as a_file:

                # get serialized objects
                saved_instances = json.load(a_file)
            # get dictionary of classes
            class_name = self.classes()

            # Use the JSON decoded objects to create object instances base on
            # <classs name> using the dictionary of classes now stored in the
            # variable <class_name> from the method <classes()> and update
            # __objects with the instances by utilizing dictionary complession
            self.__objects.update(
                {key: class_name[saved_instances[key]["__class__"]](
                    **saved_instances[key]) for key in saved_instances})

        except FileNotFoundError:
            pass  # pass for now

    def delete(self, obj=None):
        """ delete an object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()

    def attributes(self):
        """Returns a dictionary mapping class names to dictionaries
        of attribute names and types"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
