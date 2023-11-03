# Scalene triangle: All sides have different lengths
# Isoceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.
# Niraj Dave

a = int(input("length of side a = "))
b = int(input("length of side b = "))
c = int(input("length of side c = "))

if a != b and b != c and c != a:
    print("This is an Scalene triangle ")
elif a == b and b == c:
    print("This is an Equilateral trianglle")
else:
    print("Tihis is an Isosceles triangle")
