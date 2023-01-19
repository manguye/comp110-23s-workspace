"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730411646"


chardle_word: str = input("Enter a 5-character word: ")

if (len(chardle_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

chardle_character: str = input("Enter a single character: ")

if (len(chardle_character) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + chardle_character + " in " + chardle_word)
chardle_match = 0

if (chardle_character == chardle_word[0]):
    print(chardle_character + " found at index 0 ")
    chardle_match = chardle_match + 1
if (chardle_character == chardle_word[1]):
    print(chardle_character + " found at index 1 ")
    chardle_match = chardle_match + 1
if (chardle_character == chardle_word[2]):
    print(chardle_character + " found at index 2 ")
    chardle_match = chardle_match + 1
if (chardle_character == chardle_word[3]):
    print(chardle_character + " found at index 3 ")
    chardle_match = chardle_match + +1
if (chardle_character == chardle_word[4]):
    print(chardle_character + " found at index 4 ")
    chardle_match = chardle_match + 1

if (chardle_match == 0):
    print("No instances of " + chardle_character + " found in " + chardle_word)
else: 
    if (chardle_match == 1):
        print(str(chardle_match) + " instance of " + chardle_character + " found in " + chardle_word)
    else:
        print(str(chardle_match) + " instances of " + chardle_character + " found in " + chardle_word)