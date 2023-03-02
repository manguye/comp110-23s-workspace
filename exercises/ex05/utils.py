"""Function skeletons for exercise five."""

__author__ = "730411646"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of integers, returns a list of only even integers."""
    ys: list[int] = list()
    for number in xs:
        if number % 2 == 0:
            ys.append(number)
    return ys


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Given two lists of integers, combines them by appending the second to the end of the first."""
    zs: list[int] = list()
    for number in xs:
        zs.append(number)
    for number in ys:
        zs.append(number)
    return zs
