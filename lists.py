example = list() # by using constructor
example2 = [] # most common use

primes = [2,3,5,7,11,13]
primes.append(17)
primes.append(19)

print(primes) # in lists order matters

# acces to an element by index

print(primes[0]) # 1 element
print(primes[1]) # 2 element
print(primes[2]) # 3 element
print(primes[-1]) # last element
print(primes[-2]) # last - 2 element

# slice
print(primes[2:5])
print(primes[:6])

# lists can contain integers, booleans, strings, floats, and other lists
example3 = [128, True, "Alpha", 1.732, [64, False]]

#Concatenation
numbers = [1,2,3]
letters = ["a", "b", "c"]

print(numbers + letters)
print(letters + numbers)
