def remove_duplicates(elements):
    new_set = set()
    for e in elements:
        new_set.add(e)
    return list(new_set)


print(remove_duplicates([1, 1, 2, 2, 3, 3, "a", "a", "a", "b"]))
