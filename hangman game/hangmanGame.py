from random import choice
import ascii_hangman
import time

"""This project allowed me to strengthen my understanding of core programming concepts,
 including modular code design with functions, string manipulation, and game loop logic.
  I focused on creating a clean user experience by integrating ASCII art and handling real-time user input to track remaining trials.
   It was a great exercise in translating logic into a playable application."""

def update(guessed_word_list,target,user_guess):
    """This function returns updated version of the guessed word"""
    correct_guess_counter = 0
    if user_guess in target:
        for i in range(len(target)):
            if target[i] == user_guess:
                if guessed_word_list[i] != user_guess:
                    guessed_word_list[i] = user_guess
                correct_guess_counter += 1
    return "".join(guessed_word_list),correct_guess_counter

#============================================================
#      **************** Main Function *****************
#============================================================

def main():
    trials = len(ascii_hangman.hangman_ascii)-1

    print("Welcome to Hangman game")
    print("You have to guess the hidden word correctly to win")
    print("Let's Get Started!")
    print()
    print("="*60)

    wrong_guessed_letters = [] #Here we will store the wrong guessed letters to save the user's trials score

    secret_word = choice(["bill"])

    print()
    guessed_word = "_"*len(secret_word)
    guessed_word_list = list(guessed_word)
    print(ascii_hangman.hangman_ascii[trials])

    while trials and guessed_word != secret_word: #The loop conditions are: trials end or word guessed
        #show the user his progress
        print(guessed_word)
        print(f"You have {trials} trials")

        user_guess = input("Enter your guess: ").lower().strip()
        new_guessed, guessed_no = update(guessed_word_list,secret_word,user_guess)

        if new_guessed != guessed_word: #If a change happened to the word, there has been a correct guess
            for i in range(guessed_no):
                print("Correct guess")
                time.sleep(.5)
                if i > 0:
                    print("Pretty brilliant")

            guessed_word = new_guessed

            #if guessed word completed
            if guessed_word == secret_word:
                print("Congratulations!")
                print("You have guessed all word letters accurately! ")

        else:
            print("Wrong guess")
            if user_guess not in wrong_guessed_letters:
                trials -= 1
                print(ascii_hangman.hangman_ascii[trials])
                wrong_guessed_letters.append(user_guess)
            print()
main()