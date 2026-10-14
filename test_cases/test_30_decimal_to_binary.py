import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_standard_decimal():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(15) == "1111"
    assert decimal_to_binary(42) == "101010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_powers_of_two():
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(16) == "10000"
    assert decimal_to_binary(64) == "1000000"


def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)
