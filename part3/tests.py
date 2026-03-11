import sys
sys.path.insert(0, '.')

from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.is_admin is False
    assert user.id is not None
    print("✅ User creation test passed!")

def test_user_validation():
    try:
        User(first_name="", last_name="Doe", email="test@test.com")
        assert False
    except ValueError:
        pass
    try:
        User(first_name="John", last_name="Doe", email="invalid-email")
        assert False
    except ValueError:
        pass
    print("✅ User validation test passed!")

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("✅ Amenity creation test passed!")

def test_place_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    place = Place(title="Cozy Apt", description="Nice", price=100,
                  latitude=37.7, longitude=-122.4, owner=owner)
    assert place.title == "Cozy Apt"
    assert place.owner == owner
    print("✅ Place creation test passed!")

def test_place_relationships():
    owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    place = Place(title="Cozy Apt", description="Nice", price=100,
                  latitude=37.7, longitude=-122.4, owner=owner)
    review = Review(text="Great!", rating=5, place=place, user=owner)
    place.add_review(review)
    amenity = Amenity(name="Wi-Fi")
    place.add_amenity(amenity)
    assert len(place.reviews) == 1
    assert len(place.amenities) == 1
    print("✅ Place relationships test passed!")

def test_review_validation():
    user = User(first_name="Bob", last_name="M", email="bob@example.com")
    owner = User(first_name="Alice", last_name="S", email="alice2@example.com")
    place = Place(title="Test", description="", price=50,
                  latitude=0, longitude=0, owner=owner)
    try:
        Review(text="Good", rating=6, place=place, user=user)
        assert False
    except ValueError:
        pass
    try:
        Review(text="", rating=3, place=place, user=user)
        assert False
    except ValueError:
        pass
    print("✅ Review validation test passed!")

def test_update_method():
    import time
    user = User(first_name="John", last_name="Doe", email="john2@example.com")
    old_ts = user.updated_at
    time.sleep(0.01)
    user.update({"first_name": "Jane"})
    assert user.first_name == "Jane"
    assert user.updated_at > old_ts
    print("✅ Update method test passed!")


if __name__ == "__main__":
    print("\n=== Running HBnB Model Tests ===\n")
    test_user_creation()
    test_user_validation()
    test_amenity_creation()
    test_place_creation()
    test_place_relationships()
    test_review_validation()
    test_update_method()
    print("\n🎉 All tests passed!\n")
