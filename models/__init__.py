#!/usr/bin/python3
from models.base_model import storage_type
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif storage_type == "fs":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
else:
    raise ValueError("Invalid storage type")
    exit(1)

storage.reload()
