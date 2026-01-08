def check_age(age: int) -> str:
    """
    Determines if a person is a minor or adult.

    Args:
        age (int): person's age

    Returns:
        str: 'Minor' or 'Adult'
    """
    if age < 18:
        return "Minor"
    else:
        return "Adult"
    
print(check_age(88))
print(check_age(0))