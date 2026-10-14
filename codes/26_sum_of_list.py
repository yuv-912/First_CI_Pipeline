"""Program 26: Find the Sum of Elements in a List."""


def sum_of_list(numbers):
    """Calculate the sum of all elements in a list without using sum().

    - Uses a loop to accumulate the total.
    - An empty list returns 0.
    """
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print("Numbers:", nums)
    print("Sum:", sum_of_list(nums))
