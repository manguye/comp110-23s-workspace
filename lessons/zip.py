"""Challenge Question for Dict Function Writing."""

__author__ = "730411646"

def zip(xs: list[str], ys: list[int]) -> dict[str, int]:
    """Should produce a list where keys are strings and values are integers."""
    zs: dict[str, int] = {}
    i: int = 0
    if len(xs) != len(ys) or len(xs) == 0 or len(ys) == 0:
        return zs
    while i < len(xs):
        zs[xs[i]] = ys[i]
        i += 1
    return zs