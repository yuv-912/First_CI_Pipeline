import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_standard_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_k_larger_than_length():
    assert rotate_list([1, 2, 3], 7) == [3, 1, 2]


def test_negative_k_rotates_left():
    assert rotate_list([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]


def test_empty_list():
    assert rotate_list([], 5) == []


def test_k_equals_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_original_list_not_modified():
    original = [1, 2, 3, 4]
    copy_original = list(original)
    result = rotate_list(original, 2)
    assert result == [3, 4, 1, 2]
    assert original == copy_original
