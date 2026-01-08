def greet_user(name: str) -> str:
    """
    Returns a greeting message for the user.

    Args:
        name (str): user's name

    Returns:
        str: greeting message
    """
    name = input("Please enter your name: ").capitalize()

    return f"Hello {name}"

print(greet_user())

# Key points:
# - .capitalize() - Makes first character uppercase and all others lowercase
# - .upper() - Converts all characters to uppercase
# - .isupper() - Returns True if all alphabetic characters are uppercase, else False