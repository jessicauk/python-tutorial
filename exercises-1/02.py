def remove_duplicates(elements):
    """
    Remove duplicates from a list and return a new list.

    Args:
        elements (list): The list containing the elements.

    Returns:
        list: A new list without duplicates.
    """
    new_set = set()
    for e in elements:
        new_set.add(e)
    return list(new_set)


print(remove_duplicates([1, 1, 2, 2, 3, 3, "a", "a", "a", "b"]))
