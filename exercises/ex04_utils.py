"""Recreating utility functions for better understanding."""


def all(xs: list[int], x: int) -> bool:
    """Given a list of integers and an integer, checks if they are all the same."""
    if len(xs) == 0:
        return False  
    i: int = 0
    while i <= len(xs) - 1:
        if xs[i] != x:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Determines the greatest integer from a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    x: int = input[i]
    while i <= len(input) - 1:
        if input[i] > x:
            x = input[i]
        i += 1
    return x


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Checks to see if two lists are exactly the same at every index."""
    i: int = 0
    while len(xs) < len(ys):
        xs.append(0)
    while len(ys) < len(xs):
        ys.append(0)
    while i < len(xs) or i < len(ys):
        if xs[i] != ys[i]:
            return False
        i += 1
    return True