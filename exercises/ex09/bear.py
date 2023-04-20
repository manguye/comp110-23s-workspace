"""File to define Bear class."""

__author__ = "730411646"


class Bear:
    """Everything for making bears."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Spawning bears."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Bears getting older and hungrier."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bears eating."""
        self.hunger_score += num_fish
        return None