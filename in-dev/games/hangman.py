import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

print(logo)

game_is_finished = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = len(stages) - 1

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    clear()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    # Check if user has got all letters.
    if "_" not in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
