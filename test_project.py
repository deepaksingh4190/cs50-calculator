import pytest
from project import add, subtract, multiply, divide


def test_add():
    assert 10 + 2 == 12.0
    assert 10 + 5 == 15.0

def test_subtract():
    assert 10 - 2 == 8.0
    assert 10 - 5 == 5.0

def test_multiply():
    assert 10 * 2 == 20.0
    assert 10 * 5 == 50.0

def test_divide():
    assert 10 / 2 == 5.0
    assert 10 / 5 == 2.0
    with pytest.raises(ZeroDivisionError):
        10 / 0


def main():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

if __name__ == "_main_":
    main()
