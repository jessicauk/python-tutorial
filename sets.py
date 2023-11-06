import math

example = set()
print(dir(example))
print(help(example.add))
example.add(42)
example.add(False)
example.add(math.pi)
example.add("Thorium")
print(example)
example.add(42)
print(example)
print(len(example))
example.remove(42)
print(example)
print(help(example.discard))
example.discard(50)

example2 = set([28, True, 2.7, "Helium"])
print(len(example2))

example2.clear()
print(len(example2))

# Integers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

# Union
print(odds.union(evens))
print(evens.union(odds))
print(primes.union(composites))

# Intersection
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds))

# Is in
print(2 in primes)
print(6 in odds)
print(9 not in evens)
