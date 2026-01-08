def count_even_numbers(n: int) -> int:
    """
    Counts how many even numbers exist from 1 to n.

    Args:
        n (int): upper limit

    Returns:
        int: count of even numbers
    """
    count = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            count = count + 1

    return count

print(count_even_numbers(90))

# Key points:
# - The modulo operator (%) checks for divisibility. i % 2 == 0 means i is even.
# - The range(1, n + 1) ensures the loop includes n itself.
# - Using count = count + 1 increments the counter each time an even number is found.