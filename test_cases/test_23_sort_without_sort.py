import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_and_single_element():
    assert bubble_sort([]) == []
    assert bubble_sort([42]) == [42]


def test_with_duplicates_and_negatives():
    assert bubble_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_original_list_not_modified():
    original = [4, 3, 2, 1]
    original_copy = list(original)
    result = bubble_sort(original)
    assert result == [1, 2, 3, 4]
    assert original == original_copy  # original list must stay untouched
