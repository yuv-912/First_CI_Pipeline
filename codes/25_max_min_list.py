"""Program 25: Find the Maximum and Minimum in a List."""


def find_max_min(numbers):
    """Find maximum and minimum values in a list without using max() or min().

    Returns a tuple: (maximum, minimum).
    Raises ValueError for an empty list.
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return (maximum, minimum)


if __name__ == "__main__":
    nums = [4, 9, 1, 7]
    print("Numbers:", nums)
    print("(Max, Min):", find_max_min(nums))
