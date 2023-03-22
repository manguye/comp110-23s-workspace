"""EX06 - Choose Your Own Adventure."""

__author__ = "730411646"


from random import randint
points: int = 0
player: str = ""
BAD_SCORE: str = "\U0001F62D"
OKAY_SCORE: str = "\U0001F928"
GOOD_SCORE: str = "\U0001F642"
GREAT_SCORE: str = "\U0001F929"


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
            points += randint(1, 10)
            print(f"Thanks to adding {conventional_toppings[ct_idx]}, your review score is now {points}! ")
            player_choice = input(f"Would you like to add another 'conventional' topping, something 'unusual', or 'present' your pizza, Chef {player}? ")
            while player_choice != "present" and player_choice != "conventional" and player_choice != "unusual":
                player_choice = input("That wasn't one of the available options! Pick again from 'conventional', 'unusual', or 'present'! ")
        if player_choice == "unusual":
            unusual_topping: str = input(f"What do you plan on adding, Chef {player}? ")
            unusuality: int = unusual_topping_function(len(unusual_topping), points)
            points += unusuality
            print(f"Thanks to adding {unusual_topping}, your review score is now {points}! ")
            player_choice = input(f"Chef {player}, would you like to add anything else 'unusual', add something 'conventional', or 'present' your pizza? ")
            while player_choice != "present" and player_choice != "conventional" and player_choice != "unusual":
                player_choice = input("That wasn't one of the available options! Pick again from 'conventional', 'unusual', or 'present'! ")
    print(f"Your pizza got a review score of {points}!")
    if points > 1000:
        print(f"Congratulations, Chef {player}! The judges loved your pizza and gave you first place! {GREAT_SCORE}")
    elif points > 500:
        print(f"Well done, Chef {player}! Although you weren't able to take first place, you still did well in the competition! {GOOD_SCORE}")
    elif points > 100:
        print(f"Not bad, Chef {player}. You could've done better, but you weren't the worst; better luck next time! {OKAY_SCORE}")
    else:
        print(f"Chef {player}, you had to be trying to get a score this low! {BAD_SCORE}")
    

def greet() -> None:
    """Welcome message."""
    global player
    print("Pizzamaking is no easy feat, but you're here to wow the crowd with your exceptional ideas. You've come to an international pizzamaking competition to make a combination that'll impress the judges. Get as high a review score as you can and aim for first place!")
    player = input("What is your name, chef? ")


def unusual_topping_function(x: int, y: int) -> int:
    """Given a custom topping, awards or detracts randomly calculated score based on if the points value is even or odd."""
    if y % 2 == 0:
        x = x * randint(1, 10)
        return x
    else:
        x = x * randint(-10, -1)
        return x


if __name__ == "__main__":
    main()