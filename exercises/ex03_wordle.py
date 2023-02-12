"""EX03 - Wordle but with more turns."""

__author__: "730411646"

def contains_char(secret_word: str, character_check: str) -> bool:
    """Checks to see if a given character is in the secret word."""
    assert len(character_check) == 1
    character_idx: int = 0
    character_contained: bool = False
    while not character_contained and character_idx < len(secret_word):
        if character_check == secret_word[character_idx]:
            character_contained = True
        else:
            character_idx = character_idx + 1 
    if character_contained:
        return True
    else:
        return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Displays reponse regarding correctness of guess word."""
    assert len(guess_word) == len (secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    response: str = ""
    idx: int = 0
    while idx < len(secret_word):
        if guess_word[idx] == secret_word[idx]:
            response = response + GREEN_BOX
        else:
            character_checker: bool = contains_char(secret_word,guess_word[idx])
            if character_checker:
                response = response + YELLOW_BOX
            else:
                response = response + WHITE_BOX
        idx = idx + 1
    return response

def input_guess(word_length: int) -> str:
    """Checks to see if a given guess is the required length."""
    input_word: str = input(f"Enter a {word_length} character word: ")
    while len(input_word) != word_length:
        input_word = input(f"That wasn't {word_length} chars! Try again: ")
    return input_word