"""Dictionary for exercise 07."""

__author__ = "730411646"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Given a dictionary input, should return a dictionary that inverts the keys and values."""
    ys: dict[str, str] = ()
    for x in xs:
        ys[xs[x]] = x
    return ys


def favorite_color(xs: dict[str, str]) -> str:
    """Given a dictionary input, should return the value that appears the most. If there is a tie, returns the value that appeared first."""

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

def count(xs: list[str]) -> dict[str, int]:
    """Given a list of strings, should return a dictionary where each key is a unique value from the list and each value is the number of times that key appeared in the input list."""