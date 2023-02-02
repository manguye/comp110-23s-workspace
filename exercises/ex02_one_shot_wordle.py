"""EX02 - One shot world homework program."""

__author__ = "730411646"

secret_word: str("python")
guess: str = input("What is your 6-letter guess? ")
while len(guess) != 0:
    print("That was not 6 letters! Try again: " + guess)