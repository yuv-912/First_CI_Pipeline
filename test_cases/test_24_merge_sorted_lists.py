import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_interleaved_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_one_empty_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([4, 5], []) == [4, 5]


def test_both_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_negative_numbers():
    assert merge_sorted_lists([-5, -1, 3], [-3, 0, 4]) == [-5, -3, -1, 0, 3, 4]