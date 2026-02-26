from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner, amenities=None):
        super().__init__()

        if price <= 0:
            raise ValueError("Price must be positive")

        if not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude")

        if not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude")

        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities = amenities or []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": {
                "id": self.owner.id,
                "first_name": self.owner.first_name,
                "last_name": self.owner.last_name
            },
            "amenities": [
                {
                    "id": amenity.id,
                    "name": amenity.name
                } for amenity in self.amenities
            ],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }