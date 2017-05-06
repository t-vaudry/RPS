import random

game = ["P","R","S"]

guess = random.randint(0,2)

#wait.... what if they expect that?

guess = guess+1

if guess > 2:

    guess = 0

output = game[guess]