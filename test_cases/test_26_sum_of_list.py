import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list


def test_positive_integers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_negative_numbers():
    assert sum_of_list([-1, 5, -3, 2]) == 3


def test_single_element():
    assert sum_of_list([42]) == 42


def test_floating_point_numbers():
    assert sum_of_list([1.5, 2.5, 3.0]) == 7.0
