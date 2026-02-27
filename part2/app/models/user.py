from app.models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()

        if not email or "@" not in email:
            raise ValueError("Invalid email")

        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty")

        if not last_name or not last_name.strip():
            raise ValueError("Last name cannot be empty")

        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }