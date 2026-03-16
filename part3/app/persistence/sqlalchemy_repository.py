from app.extensions import db


class SQLAlchemyRepository:
    """
    Repository implementation using SQLAlchemy for database persistence.
    Provides basic CRUD operations for registered models.
    """

    def __init__(self, models):
        """
        Initialize the repository with a dictionary of models.
        """
        self.models = models

    def add(self, obj_type, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    def get(self, obj_type, obj_id):
        model = self.models.get(obj_type)
        if not model:
            return None

        return db.session.get(model, obj_id)

    def get_all(self, obj_type):
        model = self.models.get(obj_type)
        if not model:
            return []

        return db.session.query(model).all()

    def delete(self, obj_type, obj_id):
        obj = self.get(obj_type, obj_id)

        if obj:
            db.session.delete(obj)
            db.session.commit()
            return True

        return False