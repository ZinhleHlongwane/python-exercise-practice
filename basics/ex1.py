
def sum_numbers(n: int) -> int:
    """
    Sums all numbers from 1 to n.

    Args:
        n (int): upper limit

    Returns:
        int: sum of numbers from 1 to n
    """
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

print(sum_numbers(35))

# Key points:
# - range(1, n + 1) goes from 1 to n inclusive.
# - total += i is shorthand for total = total + i.
# - Loops are useful for repeated tasks.
# - total → sum of numbers (add the numbers themselves)
# - total += i → adds the current number to the sum