from app.models.base_model import BaseModel
from flask_bcrypt import generate_password_hash, check_password_hash

class User(BaseModel):
    def __init__(self, email, first_name, last_name, password):
        super().__init__()

        if not email or "@" not in email:
            raise ValueError("Invalid email")

        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty")

        if not last_name or not last_name.strip():
            raise ValueError("Last name cannot be empty")

        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters")

        self.email = email
        self.first_name = first_name
        self.last_name = last_name

        # hash password
        self.password_hash = generate_password_hash(password).decode("utf8")

    # check password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }