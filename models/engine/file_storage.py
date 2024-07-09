#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# the imports above look unused, but they are needed for the eval() in reload.


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If cls is provided, returns only models of that type.
        """
        if cls:
            if not isinstance(cls, str):
                cls = cls.__name__
            obj = {}
            for k, v in self.__objects.items():
                if v.__class__.__name__ == cls:
                    obj[k] = v
            return obj
        else:
            return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def delete(self, key=None):
        """ Deletes an object from __objects """
        if key is None:
            return
        del self.__objects[key]

    def add_amenity(self, place_id, amenity_id):
        """ this isn't implmented for FileStorage """
        message = "if you were using the database, this would add "
        message += f"Amenity {amenity_id} to Place {place_id}."
        print(message)


    def close(self):
        """Call reload() method for deserializating the JSON file to objects"""
        self.reload()
