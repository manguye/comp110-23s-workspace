"""EX02 - One shot wordle homework program."""

__author__ = "730411646"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
idx: int = 0
character_checker: str = ""

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
if len(guess) == len(secret_word):
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            character_checker = character_checker + GREEN_BOX
        else:
            right_character_wrong_place: bool = False
            right_character_wrong_place_idx: int = 0
            while not right_character_wrong_place and right_character_wrong_place_idx < len(secret_word):
                if guess[idx] == secret_word[right_character_wrong_place_idx]:
                    right_character_wrong_place = True
                else:
                    right_character_wrong_place_idx = right_character_wrong_place_idx + 1
            if right_character_wrong_place:
                character_checker = character_checker + YELLOW_BOX
            else:
                character_checker = character_checker + WHITE_BOX
        idx = idx + 1    
    print(character_checker)
    if (guess == secret_word):
        print("Woo! You got it!")
    else:
        print("Not quite! Play again soon!")