"""
Module to calculate Fibonacci numbers.
"""

fibonacci_cache = {}


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If n is not a positive integer.
        ValueError: If n is less than 1.
    """
    # If we have cached the value, then return it
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value



for n in range(1, 101):
    print(n, ":", fibonacci(n))

fibonacci(4)
