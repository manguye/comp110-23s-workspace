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


def sub(xs: list[int], x: int, y: int) -> list[int]:
    """Given a list, a start index, and an end index, creates list between the specified start and end indices."""
    ys: list[int] = list()
    if len(xs) == 0 or x >= len(xs) or y <= 0:
        return ys
    if x < 0:
        x = 0
    if y > len(xs):
        y = len(xs) - 1
    for i in range(x, y):
        if i != x or y:
            ys.append(xs[i])
    return ys