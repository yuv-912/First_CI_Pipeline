"""Program 29: Check Armstrong Number."""


def is_armstrong(number):
    """Check if a number is an Armstrong (narcissistic) number.

    A number is an Armstrong number if the sum of its digits,
    each raised to the power of the number of digits, equals the number.
    Negative numbers return False.
    """
    if number < 0:
        return False

    digits_str = str(number)
    power = len(digits_str)

    total = 0
    for digit in digits_str:
        total += int(digit) ** power

    return total == number


if __name__ == "__main__":
    n = 153
    print(f"Is {n} an Armstrong number?", is_armstrong(n))
