fibonacci_cache = {}


def fibonacci(n):
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

fibonacci("s")