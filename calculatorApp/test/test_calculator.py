import pytest
from calculatorApp.app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 5) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ValueError):
        divide(1, 0)  # Testing division by zero should raise a ValueError
