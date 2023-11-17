import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)

test1 = 1,
test2 = 1,2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print(age)
print(country)
print(knows_python)
