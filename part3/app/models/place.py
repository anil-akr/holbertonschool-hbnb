from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, price, owner_id, amenity_ids=None):
        super().__init__()

        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        if price < 0:
            raise ValueError("Price must be positive")

        if not owner_id:
            raise ValueError("Owner ID is required")

        self.title = title
        self.price = price
        self.owner_id = owner_id
        self.amenity_ids = amenity_ids or []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "owner_id": self.owner_id,
            "amenity_ids": self.amenity_ids,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }