from typing import List


def square_elements(number_list: List[int]):
    """
    Square each element in the given list.

    Args:
        number_list (List[int]): The list of numbers.

    Returns:
        List[int]: The list of squared numbers.
    """
    try:
        return [number**2 for number in number_list]
    except TypeError as exc:
        raise TypeError("Type number list should be integer") from exc


print(square_elements([2, 3, 4]))
