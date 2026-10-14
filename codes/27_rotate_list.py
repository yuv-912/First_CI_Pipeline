"""Program 27: Rotate a List by K Positions."""


def rotate_list(items, k):
    """Rotate a list to the right by k positions.

    - Returns a new list.
    - k can be larger than list length.
    - Negative k rotates to the left.
    - Empty list returns [].
    """
    if not items:
        return []

    n = len(items)
    k = k % n

    if k == 0:
        return list(items)

    return list(items[-k:] + items[:-k])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Original:", nums)
    print("Rotated right by 2:", rotate_list(nums, 2))
    print("Rotated left by 1:", rotate_list(nums, -1))
