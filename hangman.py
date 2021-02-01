import random
import string
from words import words


def get_valid_word(words1):
    word = random.choice(words1)
    while '-' in word or ' ' in word:
        word = random.choice(words1)

    return word.upper()


def hangman():
    word = get_valid_word(words)  # letter in the word correctly guessed
    word_letters = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # what the current word is; with guessed letters and letters not guessed(i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))  # creating a word using word_list list

        # get user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives-1
                print(f"Letter {user_letter} not in word")

        elif user_letter in used_letters:
            print("You just guessed that character. Please try again.")

        else:
            print("Invalid character. Please try again")
        # when loop gets here len(word_letter) == 0
    if lives == 0:
        print(f"You died!. The word was {word}.")
    else:
        print(f"You guessed the word {word} correctly!!")


hangman()
