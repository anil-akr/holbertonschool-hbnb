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