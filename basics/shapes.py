def draw_rectangle(width: int, height: int) -> str:
    """
    Draws a rectangle using '*'.

    Args:
        width (int): rectangle width
        height (int): rectangle height

    Returns:
        str: rectangle as a string
    """
    rectangle = ""

    for row in range(height):
        rectangle = rectangle + "*" * width
        rectangle = rectangle + "\n"

    return rectangle

print(draw_rectangle(8, 9))

# Key points:
# - "*" * width creates a single row of stars.
# - "\n" moves to the next line so rows stack vertically.
# - Looping 'height' times repeats this process for all rows.
# - Using '+=' adds each new row to the existing rectangle string.
# - Returning the full string allows us to print the rectangle neatly.
