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