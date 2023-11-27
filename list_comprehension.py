"""
This script demonstrates the usage of list comprehension in Python.
It includes examples of creating a list of squares, calculating remainders,
filtering movies starting with the letter 'G', and finding movies by a given year.
"""

from typing import List, Tuple

list_squares = [number**2 for number in range(1, 101)]
print(list_squares)

print("*" * 4**3)

reminders5 = [x**2 % 5 for x in range(1, 101)]
print(reminders5)


print("*" * 4**3)


def g_movies(movies_list: List[str]) -> List[str]:
    """Get movies fron the list which starts with the letter 'G'"""
    return [movie for movie in movies_list if movie.startswith("G")]


movies = [
    "Star Wars",
    "Gandhi",
    "Casablanca",
    "Shawshank Redemption",
    "Toy Story",
    "Gone with the Wind",
    "Citizen Kane",
    "It's a Wonderful Life",
    "The Wizard of Oz",
    "Gattaca",
    "Rear Window",
    "Ghostbusters",
    "To Kill A Mockingbird",
    "Good Will Hunting",
    "2001: A Space Odyssey",
    "Raiders of the Lost Ark",
    "Groundhog Day",
    "Close Encounters of the Third Kind",
]

print(g_movies(movies))
print("*" * 4**3)


movies_tuple = [
    ("Citizen Kane", 1941),
    ("Spirited Away", 2001),
    ("It's a Wonderful Life", 1946),
    ("Gattaca", 1997),
    ("No Country for Old Men", 2007),
    ("Rear Window", 1954),
    ("Star Wars", 2000),
    ("Gandhi", 200),
    ("The Lors of the Rings: The Fellowship of the Ring", 2001),
    ("Groundhog Day", 1993),
    ("Close Encounters of the Third Kind", 1977),
    ("The Royal Tenenbaums", 2001),
    ("The Aviator", 2004),
    ("Raiders of the Lost Ark", 1981),
]


def find_movie(year: int, movies_list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Find a movie by a given year"""
    return [
        (title, movie_year) for title, movie_year in movies_list if movie_year == year
    ]


print(find_movie(2001, movies_tuple))

print("*" * 4**3)

# Cartesian Product

A = [1, 3, 4, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)

# End-of-file (EOF)
