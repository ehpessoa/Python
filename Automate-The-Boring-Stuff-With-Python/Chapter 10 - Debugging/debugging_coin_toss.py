#! python3
# debugging_coin_toss.py - Debug this

# input is case sensitive
import random

heads_or_tails = ['heads', 'tails']
toss = random.choice(heads_or_tails)

guess = ''
while guess not in heads_or_tails:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = ''
    while guess not in heads_or_tails:
        guess = input().lower()

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
