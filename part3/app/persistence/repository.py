from app.persistence.sqlalchemy_repository import SQLAlchemyRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place


models = {
    "User": User,
    "Amenity": Amenity,
    "Place": Place
}

# Global repository instance used by the facade
repository = SQLAlchemyRepository(models)