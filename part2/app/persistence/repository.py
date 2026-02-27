class InMemoryRepository:
    def __init__(self):
        self.storage = {
            "User": {},
            "Amenity": {},
            "Place": {}
        }

    def add(self, obj_type, obj):
        self.storage[obj_type][obj.id] = obj

    def get(self, obj_type, obj_id):
        return self.storage[obj_type].get(obj_id)

    def get_all(self, obj_type):
        return list(self.storage[obj_type].values())

    def delete(self, obj_type, obj_id):
        if obj_id in self.storage[obj_type]:
            del self.storage[obj_type][obj_id]
            return True
        return False


# Instance globale utilisée par le facade
repository = InMemoryRepository()