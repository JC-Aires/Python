"""
Name: hangmanv2.py
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


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

global word
chosen_word = get_valid_word(words_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# print(f'Pssst, the solution is {chosen_word}.')  # Testing code

display = []  # Create blanks for the word length
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")  # Join all the elements in the list and turn it into a string.

while not end_of_game:

    guess = input("Guess a letter: ").upper()

    for position in range(word_length):  # Check if guessed letter is in the word
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:  # If guess is not a letter in the chosen_word, reduce 'lives' by 1.
        lives -= 1
        if lives == 0:  # Ends game if all tries(lives) are gone
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:  # Check if user has got all letters.
        end_of_game = True
        print("You win.")

    print(stages[lives])  # Print the figure from 'stages' variable that equals the current number of 'lives' remaining.
