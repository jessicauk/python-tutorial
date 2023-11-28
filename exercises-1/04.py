def reverse_number(number: int) -> int:
    """
    Reverses the digits of a given number.

    Args:
        number (int): The number to be reversed.

    Returns:
        int: The reversed number.
    """
    
    return int(str(number)[::-1])

print(reverse_number(625235))