"""File to define Fish class."""

__author__ = "703411646"


class Fish:
    "Everything for making fish."

    age: int
    
    def __init__(self):
        "Spawning fish."
        self.age = 0
        return None
    
    def one_day(self):
        "Fish getting older."
        self.age += 1
        return None