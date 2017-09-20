from main_fibonacci_function import fibonacci
import pytest


def test_fibonacci_1():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected


def test_fibonacci_2():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected


def test_fibonacci_3():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected


def test_fibonacci_4():
    with pytest.raises(ValueError) as e:
        fibonacci(-5)
    assert e.value.message == "The input value is incorrect: -5"


def test_fibonacci_5():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected


def test_fibonacci_6():
    expected = 55
    actual = fibonacci(10)
    assert actual == expected
