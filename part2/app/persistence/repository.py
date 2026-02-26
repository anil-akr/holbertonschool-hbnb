from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository:
    def __init__(self):
        self._storage = {
            "User": {},
            "Place": {},
            "Review": {},
            "Amenity": {}
        }

    def add(self, obj_type, obj):
        self._storage[obj_type][obj.id] = obj

    def get(self, obj_type, obj_id):
        return self._storage[obj_type].get(obj_id)

    def get_all(self, obj_type):
        return list(self._storage[obj_type].values())

    def update(self, obj_type, obj_id, data):
        obj = self.get(obj_type, obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_type, obj_id):
        return self._storage[obj_type].pop(obj_id, None)
