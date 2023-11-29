import math


def is_prime(num: int):
    """Return 'True' if 'num' is a prime number. False otherwise."""
    if num == 1:
        return False  # 1 is not a prime
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(num))  # round down
    for d in range(3, 1 + max_divisor, 2):
        if num % d == 0:
            return False
    return True

# Test function
SUM_PRIMES = 0
for n in range(1, 200000):
    if is_prime(n):
        SUM_PRIMES += n
print("sum_primes", SUM_PRIMES)
