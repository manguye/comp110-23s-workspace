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
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    x: int = 0
    while i <= len(input) - 1:
        if input[i] > x:
            x = input[i]
        i += 1
    return x