import random
from guess_number_art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Function to check user's guess against actual answer. 
    Passes guess, answer, turns"""

    if guess > answer:
        print("Too high.")
        return turns - 1

    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    """Function to set difficulty, easy or hard"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """Function that starts the guess number game"""
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    # Used to test code
    # print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out if guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")


game()
