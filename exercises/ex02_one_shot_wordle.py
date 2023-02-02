"""EX02 - One shot world homework program."""

__author__ = "730411646"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
if len(guess) == len(secret_word):    
    if (guess == secret_word):
        print("Woo! You got it!")
    else:
        print("Not quite! Play again soon!")