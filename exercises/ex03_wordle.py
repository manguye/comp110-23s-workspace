"""EX03 - Wordle but with more turns."""

__author__: "730411646"

def contains_char(secret_word: str, character_check: str) -> bool:
    """Checks to see if a given character is in the secret word."""
    assert len(character_check) == 1
    idx: int = 0
    character_contained: bool = False
    while not character_contained and idx < len(secret_word):
        if character_check == secret_word[idx]:
            character_contained = True
        else:
            idx = idx + 1 
    if character_contained:
        return True
    else:
        return False