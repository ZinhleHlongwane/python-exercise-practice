def string_to_integer(text: str) -> int:
    """
    Converts a numeric string into an integer.

    Args:
        text (str): numeric string

    Returns:
        int: converted integer
    """
    try:
        return int(text)
    except ValueError:
        print(f"Warning: '{text}' is not a valid interger, Returning 0")
        return 0

print(string_to_integer("456"))
print(string_to_integer("abc"))

# Key points:
# - int(text) converts a string containing digits into an integer.
# - If the string is not numeric (like "abc"), it will raise a ValueError.
# - You can handle errors with try-except if needed for more robust code.