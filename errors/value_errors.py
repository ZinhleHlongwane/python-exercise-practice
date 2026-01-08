def safe_int_convert(text: str) -> int:
    """
    Safely converts a string to an integer.

    Args:
        text (str): numeric string

    Returns:
        int: converted number
    """
    return int(text)

print(safe_int_convert("456"))