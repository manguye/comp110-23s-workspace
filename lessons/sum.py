"""Example function for unit tests with for ... in ... loops and range."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs"""
    sum_total: float = 0.0
    i: int = 0
    for i in range(0, len(xs)):
        sum_total += xs[i]
        i += 1
    return sum_total