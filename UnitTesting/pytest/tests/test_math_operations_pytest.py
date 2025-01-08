from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3)  == -5

def test_add_mixed_numbers():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
