# models/entity.py

class Entity:
    _id_counter = 1

    def __init__(self):
        self.id = self.__class__._id_counter
        self.__class__._id_counter += 1
