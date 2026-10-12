"""Program 22: Check Anagram Strings."""


def is_anagram(first, second):
    """Check if two strings are anagrams, ignoring case and spaces.

    Returns True or False.
    """
    clean_first = [c for c in first.lower() if not c.isspace()]
    clean_second = [c for c in second.lower() if not c.isspace()]
    return sorted(clean_first) == sorted(clean_second)


if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print("Are anagrams:", is_anagram(str1, str2))
