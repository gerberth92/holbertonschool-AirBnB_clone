#!/urs/bin/python3
from models.base_model import BaseModel
from models.user import User
import json
from os.path import exists

clases = {"BaseModel": BaseModel, "User": User}

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new = {}
        for clave, valor in self.__objects.items():
            new[clave] = valor.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as archivo:
            json.dump(new, archivo)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as doc:
                for clave, valor in json.load(doc).items():
                    if valor["__class__"] in clases:
                        clase = clases[valor["__class__"]]
                        self.__objects[clave] = clase(**valor)
