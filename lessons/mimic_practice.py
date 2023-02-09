def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Index too high")
    #If we made it here, that means letter_idx is valid
    return my_words[letter_idx]

my_words: str = input("Word: ")
letter_idx: int = int(input("Number: "))
letter: str = mimic_letter(my_words,letter_idx)
print(letter)