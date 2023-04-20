"""File to define River class."""

__author__ = "730411646"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Everything that you may possibly think of with a river, fish, and bears. This statement is not legally binding."""

    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Culling the old."""
        new_fish: list[Fish] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for x in self.bears:
            if x.age <= 5:
                new_bears.append(x)
        self.bears = new_bears
        return None

    def bears_eating(self):
        """Feeding the hungry."""
        for x in self.bears:
            if len(self.fish) >= 5:
                x.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Culling those too hungry."""
        nonstarving: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                nonstarving.append[x]
        self.bears = nonstarving
        return None
        
    def remove_fish(self, amount: int):
        """Removing the food."""
        while amount > 0:
            self.fish.pop(0)
            amount -= 1
        return None

    def repopulate_fish(self):
        """Getting new fish."""
        birth_rate: int = (len(self.fish) // 2) * 4
        while birth_rate > 0:
            self.fish.append(Fish())
            birth_rate -= 1
        return None
    
    def repopulate_bears(self):
        """Getting new bears."""
        birth_rate: int = len(self.bears) // 2
        while birth_rate > 0:
            self.bears.append(Bear())
            birth_rate -= 1
        return None
    
    def view_river(self):
        """Checking progress."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        self.one_river_day
        return None
