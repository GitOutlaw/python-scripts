from random import randint

num = randint(1, 20)
guess = 0
guess_count = 1
while guess is not num:
if guess_count <= 3:
guess = input('Please guess a number between 1-20, you have three guesses: ')
guess = int(guess)
if guess > 20:
print(‘PLease select a number between 1-20’)