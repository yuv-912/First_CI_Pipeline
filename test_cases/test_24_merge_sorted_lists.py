import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_interleaved_lists():
    # Both lists have elements that interleave
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_one_empty_list():
    # One list has numbers, the other is completely empty
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([4, 5], []) == [4, 5]


def test_both_empty_lists():
    # Edge case: both lists are empty
    assert merge_sorted_lists([], []) == []


def test_duplicates():
    # Lists containing duplicate values
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_negative_numbers():
    # Lists with negative numbers
    assert merge_sorted_lists([-5, -1, 3], [-3, 0, 4]) == [-5, -3, -1, 0, 3, 4]