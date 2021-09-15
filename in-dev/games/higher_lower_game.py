from higher_lower_game_data import data
from higher_lower_art import logo, vs
import random
from replit import clear


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    
    # Used to debug the game.
    account_answer = account["follower_count"]
    print(f"Pssst the answer is: {account_answer}")
    
    # Used to return fstring with formatted data.
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Take the users guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    # Set intial score to 0
    score = 0
    # Used for while loop
    game_should_continue = True
    account_b = random.choice(data)

    # Makes the game repeatable.
    while game_should_continue:
        # Generate a random account from the game data.
        account_a = account_b
        account_b = random.choice(data)

        # Makes account at postition B become the next account at position A.
        while account_a == account_b:
            account_b = random.choice(data)

        # Print formatted accounts from data.
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Gets follower count of each account. Checks if user is correct. 
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen between rounds
        clear()
        # Display art.
        print(logo)

        # Give user feedback on their guess, and keep score.
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            

        else:
            game_should_continue = False
            print(f"Sorry that's wrong. Final score: {score}")

game()


