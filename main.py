"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    vowels = "aeiouAEIOU"
    count = 0

    for palavra in string:
        if palavra in vowels:
            count += 1

    return int(count)
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
