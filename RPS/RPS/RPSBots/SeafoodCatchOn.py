import random

if input == "": # initialize variables for the first round
        rockCount = paperCount = scissorsCount = 0
elif input == "R":
        rockCount += 1
elif input == "P":
        paperCount += 1
elif input == "S":
        scissorsCount += 1

outputchoice = ['R', 'P', 'S']

for r in range(rockCount / 2):
        outputchoice.append('P')
for p in range(paperCount / 2):
        outputchoice.append('S')
for s in range(scissorsCount /2 ):
        outputchoice.append('R')

random.shuffle(outputchoice)

if len(outputchoice) > random.randint(900, 1100):
        outputchoice = ['S', 'P', 'R']

output = random.choice(outputchoice)