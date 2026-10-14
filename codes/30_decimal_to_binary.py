"""Program 30: Convert Decimal to Binary Without Using bin()."""


def decimal_to_binary(number):
    """Convert a non-negative integer to binary using repeated division by 2.

    - Does not use bin().
    - Returns the binary digits as a string.
    - 0 returns "0".
    - A negative number raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers cannot be converted to binary")

    if number == 0:
        return "0"

    bits = []
    n = number
    while n > 0:
        bits.append(str(n % 2))
        n //= 2

    return "".join(reversed(bits))


if __name__ == "__main__":
    val = 10
    print(f"Decimal {val} in binary:", decimal_to_binary(val))
