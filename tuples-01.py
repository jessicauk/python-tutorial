import sys

# List example
prime_numbers = [1, 3, 5, 7, 11, 13, 17]
# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)
print("# Squares = ", len(perfect_squares))

# Iterate

for n in perfect_squares:
    print("Square: ", n)

# Tuple diff versus List
print("List methods")
print(dir(prime_numbers))
print(80 * "-")
print("Tuple methods")
print(dir(perfect_squares))
print(80 * "-")
print(dir(sys))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print(sys.getsizeof(list_eg))
print(sys.getsizeof(tuple_eg))
