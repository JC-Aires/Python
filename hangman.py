"""
Name: hangman.py
Purpose: Discover the hidden word (traditional Hangman game).
Author: JC-Aires
"""

import random
from words import words_list


def get_valid_word(words_list):  # Pick a word without dash or space (- or ' ').

    global word
    word = random.choice(words_list)  # Randomly pick a word from the list 'words_list'.
    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    return word.upper()  # Use uppercase for all comparisons


def hangman():  # Game logic

    global lives
    global word
    word = get_valid_word(words_list)
    word_letters = set(word)  # List of the unique letters in the 'word'
    used_letters = set()  # Keeps track of user letters input
    list_of_letters = list(word)  # Transform the string 'word' into a list of separate chars
    aux_display = []  # Used to display the hidden word

    for i in range(len(word)):  # Change all the letters to '-' to hide the word in the screen
        aux_display.append('-')

    while len(word_letters) > 0 and lives > 0:  # Gets user inputs
        print("\n", end='')
        print(' '.join(aux_display))
        current_letter = input("Guess the hidden word. Enter a letter: ").upper()

        if current_letter in used_letters:
            print("\nYou already used that letter. Pick another one: ")
        elif current_letter in word:
            word_letters.remove(current_letter)
            used_letters.add(current_letter)
            # Finds and change the positions of the letters in 'word" matching user input guess
            indexes = [index for index, letter in enumerate(list_of_letters) if letter == current_letter]
            for position in indexes:
                aux_display[position] = current_letter
        else:
            used_letters.add(current_letter)
            lives -= 1  # Reduce the number of tries left
            print("\nLetter not in the word! You have", lives, "tries remaining.")
            print("\nYou have used these letters: ", ' '.join(used_letters))

    return lives, word


lives = 6  # Define the number of tries before dying, set to 'global' in modules
word = ' '  # Initial variable setup, also set to 'global' in modules
hangman()
if lives == 0:
    print(f"\nGAME OVER! The word was {word}!")
else:
    print(f"\nCorrect! The hidden word was {word}.")
