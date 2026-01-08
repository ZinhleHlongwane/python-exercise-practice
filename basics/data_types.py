def describe_data(value) -> str:
    """
    Returns the type of the given value as a string.

    Args:
        value: any data type

    Returns:
        str: name of the data type
    """
    return type(value).__name__

print(describe_data(42))          
print(describe_data(3.14))        
print(describe_data("Hello"))     
print(describe_data([1, 2, 3]))   
print(describe_data({"a": 1}))

# Key points:
# - type(value) returns the type object of the value.
# - Adding .__name__ gives the name of the type as a string.
# - This works for any Python object.