"""Dictionary for exercise 07."""

__author__ = "730411646"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary input, should return a dictionary that inverts the keys and values."""
    inverse_dict: dict[str, str] = {}
    for item in original_dict:
        inverse_dict[original_dict[item]] = item
    return inverse_dict


def favorite_color(color_inputs: dict[str, str]) -> str:
    """Given a dictionary input, should return the value that appears the most. If there is a tie, returns the value that appeared first."""
    color_result: str = ""
    color_counter: dict[str, int] = {}
    for person in color_inputs:
        if color_inputs[person] in color_counter:
            color_counter[f"{color_inputs[person]}"] += 1
        else:
            color_counter[f"{color_inputs[person]}"] = 1

    return color_result

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

def count(item_list: list[str]) -> dict[str, int]:
    """Given a list of strings, should return a dictionary where each key is a unique value from the list and each value is the number of times that key appeared in the input list."""
    item_counter: dict[str, int] = {}
    for item in item_list:
        if item_list[item] in item_counter:
            item_counter[f"{item_list[item]}"] += 1
        else:
            item_counter[f"{item_list[item]}"] = 1
    return item_counter