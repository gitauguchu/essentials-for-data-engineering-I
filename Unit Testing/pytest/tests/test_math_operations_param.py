import pytest
from src.math_operations import add

@pytest.mark.parametrize(
    "a, b, expected_sum",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (2, -3, -1),
        (0, 0, 0)
    ]
)

def test_add(a, b, expected_sum):
    result = add(a, b)
    assert result == expected_sum