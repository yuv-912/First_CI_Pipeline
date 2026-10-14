"""Program 28: Find the Intersection of Two Sets."""


def set_intersection(first, second):
    """Return a set containing only the elements present in both sets.

    - Does not modify the input sets.
    - Returns a new set.
    """
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result


if __name__ == "__main__":
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print("Set 1:", s1)
    print("Set 2:", s2)
    print("Intersection:", set_intersection(s1, s2))
