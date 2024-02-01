#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """A public instance method to delete obj from __objects"""
        if obj:
            for key, val in self.__objects.items():
                if obj == val:
                    del self.__objects[key]
                    return

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        all_obj = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if cls.__name__ == value.to_dict()['__class__']:
                    all_obj[key] = value
            return all_obj
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.all().update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        import json

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                #temp = json.load(f)
                for key, val in (json.load(f)).items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
            Close: A pub method for deserializing the JSON file to objs
        """
        self.reload()
