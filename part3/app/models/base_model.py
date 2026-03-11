import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key) and key not in ["id", "created_at"]:
                setattr(self, key, value)

        self.updated_at = datetime.utcnow()