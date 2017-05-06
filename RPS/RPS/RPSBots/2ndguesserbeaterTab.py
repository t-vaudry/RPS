import random

game = ["P","R","S"]

#Oh, I know what they are going to do, I can beat this

output = game[2]

#somehow... I don't think this is going to work

guess = random.randint(0,2)

#wait.... what if they expect that?

guess = guess+1

if guess > 2:

    guess = 0

output = game[guess]

#no, dammit, I'll just stick to my guns

output = game[2]