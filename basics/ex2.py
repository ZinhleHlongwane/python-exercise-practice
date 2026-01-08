def is_palindrome(text: str) -> bool:
    """
    Checks if a string is a palindrome.

    Args:
        text (str): input string

    Returns:
        bool: True if palindrome, else False
    """
    reversed_text = text[::-1]  # Slice to reverse the string
    return text == reversed_text

print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))   # False

# Key points:
# - text[::-1] reverses a string.
# - Strings can be compared using ==.
# - Palindrome means same forwards and backwards.
