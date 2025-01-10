import pytest
from src.user import User

@pytest.fixture
def user() -> User:
    """Pytest fixture to create a User instance for testing"""
    return User(1, "John Doe", 30)

def test_user_creation(user: User) -> None:
    """Test the creation of a user instance"""
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.age == 30

def test_greet(user: User) -> str:
    """Test the greet method of a user instance"""
    greeting: str = user.greet()
    assert greeting == "Hello, my name is John Doe and I am 30 years old."