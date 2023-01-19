"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730411646"


chardle_word: str = input("Enter a 5-character word: ")
chardle_character: str = input("Enter a single character: ")
print("Searching for " + chardle_character + " in " + chardle_word)

if (chardle_character == chardle_word[0]):
    print(chardle_character + " found at index 0 ")
if (chardle_character == chardle_word[1]):
    print(chardle_character + " found at index 1 ")
if (chardle_character == chardle_word[2]):
    print(chardle_character + " found at index 2 ")
if (chardle_character == chardle_word[3]):
    print(chardle_character + " found at index 3 ")
if (chardle_character == chardle_word[4]):
    print(chardle_character + " found at index 4 ")