"""Program 23: Sort a list without using sort() or sorted()."""


def bubble_sort(numbers):
    """Sort a list of numbers in ascending order using Bubble Sort.

    - Does not use sort() or sorted().
    - Returns a new list.
    - Does not modify the original list.
    """
    arr = list(numbers)  # Make a copy so original list is not modified
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap neighboring elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred in this pass, the list is already sorted
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    nums = [5, 2, 9, 1]
    print("Original:", nums)
    print("Sorted:", bubble_sort(nums))
