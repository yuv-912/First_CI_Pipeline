import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_three_digit_armstrong():
    assert is_armstrong(153) is True
    assert is_armstrong(370) is True
    assert is_armstrong(371) is True


def test_non_armstrong():
    assert is_armstrong(123) is False
    assert is_armstrong(100) is False


def test_negative_numbers_return_false():
    assert is_armstrong(-153) is False
    assert is_armstrong(-1) is False


def test_single_digit_numbers():
    assert is_armstrong(0) is True
    assert is_armstrong(7) is True


def test_four_digit_armstrong():
    assert is_armstrong(9474) is True
