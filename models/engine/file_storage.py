#!/urs/bin/python3
from models.base_model import BaseModel
import json
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__dict__)

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__)
        self.__objects[key] = obj

    def save(self):
        new = {}
        for clave, valor in self.__objects:
            new[clave] = valor.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as archivo:
            json.dump(new, archivo)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as doc:
                self.__objects = json.load(doc)

        for clave, valor in self.__objects.items():
            clase = globals()[valor["__class__"]]
            self.__objects[clave] = clase(**valor)
