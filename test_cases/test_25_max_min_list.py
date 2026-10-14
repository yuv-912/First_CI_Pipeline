import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_standard_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single_element():
    assert find_max_min([42]) == (42, 42)


def test_negative_numbers():
    assert find_max_min([-10, -50, -2, -8]) == (-2, -50)


def test_all_equal_elements():
    assert find_max_min([7, 7, 7, 7]) == (7, 7)


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_max_min([])
