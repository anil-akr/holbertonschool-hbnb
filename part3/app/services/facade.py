from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.persistence.repository import repository


class HBnBFacade:

    # ======================
    # USER METHODS
    # ======================

    def create_user(self, data):
        password = data.get("password")
        if not password:
            raise ValueError("Password is required")

        user = User(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=password
        )

        repository.add("User", user)
        return user

    def get_user(self, user_id):
        return repository.get("User", user_id)

    def get_all_users(self):
        return repository.get_all("User")

    def update_user(self, user_id, data):
        user = repository.get("User", user_id)
        if not user:
            return None

        user.update(data)
        return user


    # ======================
    # AMENITY METHODS
    # ======================

    def create_amenity(self, data):
        amenity = Amenity(name=data["name"])
        repository.add("Amenity", amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return repository.get("Amenity", amenity_id)

    def get_all_amenities(self):
        return repository.get_all("Amenity")

    def update_amenity(self, amenity_id, data):
        amenity = repository.get("Amenity", amenity_id)
        if not amenity:
            return None

        amenity.update(data)
        return amenity


    # ======================
    # PLACE METHODS
    # ======================

    def create_place(self, data):
        # Vérifie que le owner existe
        owner = repository.get("User", data["owner_id"])
        if not owner:
            raise ValueError("Owner not found")

        # Vérifie que les amenities existent
        amenity_ids = data.get("amenity_ids", [])
        for amenity_id in amenity_ids:
            if not repository.get("Amenity", amenity_id):
                raise ValueError(f"Amenity {amenity_id} not found")

        place = Place(
            title=data["title"],
            price=data["price"],
            owner_id=data["owner_id"],
            amenity_ids=amenity_ids
        )

        repository.add("Place", place)
        return place

    def get_place(self, place_id):
        return repository.get("Place", place_id)

    def get_all_places(self):
        return repository.get_all("Place")

    def update_place(self, place_id, data):
        place = repository.get("Place", place_id)
        if not place:
            return None

        # Si on change owner → vérifier qu'il existe
        if "owner_id" in data:
            if not repository.get("User", data["owner_id"]):
                raise ValueError("Owner not found")

        # Si on change amenities → vérifier qu'elles existent
        if "amenity_ids" in data:
            for amenity_id in data["amenity_ids"]:
                if not repository.get("Amenity", amenity_id):
                    raise ValueError(f"Amenity {amenity_id} not found")

        place.update(data)
        return place