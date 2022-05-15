#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15/05/2022 14:56
# @Author : Karim
# @Site : 
# @File : hangman.py
# @Software: IntelliJ IDEA

# create a hangman game that will randomly select a word from a list of words
# and display the word with dashes.
# the user will be prompted to guess a letter.
import random

print("Welcome to Hangman!")
print("The computer will select a word from a list of words.")
print("You will be prompted to guess a letter.")
print("If you guess a letter that is in the word, it will be displayed.")

intro = input("Press enter to begin.")

def select_word():
    words = ["python", "java", "kotlin", "javascript", "swift", "ruby", "typescript"]
    return random.choice(words)

def display_word(word, letters_guessed):
    output = ""
    for letter in word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_"
    return output

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("You can only guess a single letter.")
        elif not guess.isalpha():
            print("You can only guess letters.")
        else:
            return guess

def play_again():
    again = input("Would you like to play again? (y/n) ").lower()
    if again == "y":
        return True
    else:
        if again == "n":
            print("Thanks for playing!")
        return False


def main():
    word = select_word()
    letters_guessed = []
    guesses_left = 6
    print("The word is " + str(len(word)) + " letters long.")
    print("You have " + str(guesses_left) + " guesses left.")
    while guesses_left > 0:
        display = display_word(word, letters_guessed)
        print(display)
        guess = get_guess()
        if guess in letters_guessed:
            print("You already guessed that letter.")
        elif guess in word:
            letters_guessed.append(guess)
        else:
            print("That letter is not in the word.")
            guesses_left -= 1
        if "_" not in display:
            print("You win!")
            break
        if guesses_left == 0:
            print("You lose!")
            print("The word was " + word)
    play_again()


if __name__ == '__main__':
    main()

# Path: hangman.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15/05/2022 14:56
# @Author : Karim
# @Site :
# @File : hangman.py
# @Software: IntelliJ IDEA
