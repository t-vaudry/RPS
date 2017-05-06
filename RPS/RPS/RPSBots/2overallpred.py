import random

def next(entry):
    a = ['R', 'P', 'S']
    index = a.index(entry)
    index = index+1
    if index > 2:
        index = 0
    return a[index]

if input=="":
    output = random.choice(['R', 'P', 'S'])
    their_moves = []
else:
    their_moves.append(input)
    choice = random.choice(input)
    output = next(choice)