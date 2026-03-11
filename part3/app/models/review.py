from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, user, place):
        super().__init__()

        if not text or len(text.strip()) == 0:
            raise ValueError("Review text cannot be empty")

        self.text = text
        self.user = user
        self.place = place

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "user": {
                "id": self.user.id,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name
            },
            "place_id": self.place.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }