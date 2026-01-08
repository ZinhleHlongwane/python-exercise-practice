def calculate_sum(a: int, b: int) -> int:
    """
    Calculates the sum of two integers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum of a and b
    """
    return a + b

print(calculate_sum(3, 4))
print(calculate_sum(-3, 4))

# Key points:
# - The built-in Python function sum() does not take two separate numbers as arguments.
# - It’s meant to sum an iterable, like a list or tuple. For example: sum([1, 2, 3]) → 6.
# - Since you just want to add two numbers, you should use the + operator instead.
# - Use + to add two numbers, not sum(a, b), because sum expects an iterable: total = a + b
