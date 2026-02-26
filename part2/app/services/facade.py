from app.models.user import User
from app.persistence.repository import repository


class HBnBFacade:

    # CREATE
    def create_user(self, data):
        user = User(**data)
        repository.add("User", user)
        return user

    # GET ONE
    def get_user(self, user_id):
        return repository.get("User", user_id)

    # GET ALL
    def get_all_users(self):
        return repository.get_all("User")

    # UPDATE
    def update_user(self, user_id, data):
        user = repository.get("User", user_id)
        if not user:
            return None

        user.update(data)
        return user

from app.models.place import Place
from app.persistence.repository import repository


    def create_place(self, data):
        owner = repository.get("User", data.get("owner_id"))
        if not owner:
            return None

        amenities = []
        for amenity_id in data.get("amenity_ids", []):
            amenity = repository.get("Amenity", amenity_id)
            if amenity:
                amenities.append(amenity)

        place = Place(
            title=data["title"],
            price=data["price"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            owner=owner,
            amenities=amenities
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

        if "price" in data and data["price"] <= 0:
            raise ValueError("Price must be positive")

        if "latitude" in data and not (-90 <= data["latitude"] <= 90):
            raise ValueError("Invalid latitude")

        if "longitude" in data and not (-180 <= data["longitude"] <= 180):
            raise ValueError("Invalid longitude")

        place.update(data)
        return place

from app.models.review import Review


    def create_review(self, data):
        user = repository.get("User", data.get("user_id"))
        place = repository.get("Place", data.get("place_id"))

        if not user or not place:
            return None

        review = Review(
            text=data["text"],
            user=user,
            place=place
        )

        place.reviews.append(review)
        repository.add("Review", review)

        return review


    def get_review(self, review_id):
        return repository.get("Review", review_id)


    def get_all_reviews(self):
        return repository.get_all("Review")


    def update_review(self, review_id, data):
        review = repository.get("Review", review_id)
        if not review:
            return None

        if "text" in data and not data["text"].strip():
            raise ValueError("Review text cannot be empty")

        review.update(data)
        return review


    def delete_review(self, review_id):
        review = repository.get("Review", review_id)
        if not review:
            return None

        review.place.reviews.remove(review)
        repository.delete("Review", review_id)

        return True
