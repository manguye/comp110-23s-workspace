"""EX06 - Choose Your Own Adventure."""

__author__ = "730411646"

from random import randint
points: int = 0
player: str = ""

def main() -> None:
    """The beginning."""
    global points
    greet()
    player_choice: str = input(f"What would you like to add to your pizza, Chef {player}? Something 'conventional'? Something 'unusual'? When you're ready to be judged, type 'present'! ")
    while player_choice != "present" and player_choice != "conventional" and player_choice != "unusual":
        player_choice = input("That wasn't one of the available options! Pick again from 'conventional', 'unusual', or 'present'! ")
    while player_choice != "present":
        if player_choice == "conventional":
            ct_idx: int = -1
            conventional_toppings: list[str] = ["pepperoni", "extra cheese", "mushrooms", "onions", "sausage", "black olives", "green peppers", "pineapple", "spinach", "nothing at all"]
            while ct_idx < 0 or ct_idx > 10:
                ct_idx = int(input(f"Which of the following toppings would you like to add, Chef {player}? Input their index value! {conventional_toppings} "))
                while ct_idx < 0 or ct_idx > 10:
                    ct_idx = int(input("That's not an index value of one of the conventional toppings! Pick again! "))
            points += randint(1,10)
            print(f"Thanks to adding {conventional_toppings[ct_idx]}, your review score is now {points}! ")
            player_choice = input("Would you like to add another 'conventional' topping, something 'unusual', or 'present' your pizza? ")
    print(f"Your pizza got a review score of {points}!")

def greet() -> None:
    """Welcome message."""
    global player
    print("Pizzamaking is no easy feat, but you're here to wow the crowd with your exceptional ideas. You've come to an international pizzamaking competition to make a combination that'll impress the judges. Get as high a review score as you can and aim for first place!")
    player = input("What is your name, chef? ")

if __name__ == "__main__":
    main()