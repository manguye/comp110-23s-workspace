def all(xs: list[int], x: int) -> bool:
    """Given a list of integers and an integer, checks if they are all the same."""
    i: int = 0
    while i <= len(xs) - 1:
        if xs[i] != x:
            return False
        i += 1
    return True