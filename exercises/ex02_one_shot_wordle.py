"""EX02 - One shot world homework program."""

__author__ = "730411646"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
while len(guess) != 6:
    guess: str = input("That was not 6 letters! Try again: ")
if len(guess) == 6:    
    if (guess == secret_word):
        print("Woo! You got it!")
    else:
        print("Not quite! Play again soon!")