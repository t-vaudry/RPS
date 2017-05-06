import random

print "Starting"
if (input == "" or (roundCount % 3 == 0)):
    randomChoice = random.choice([0,1,2])
    roundCount = 0
    print "init random: " + str(randomChoice)
    output = ["R","P","S"][randomChoice]
else:
    roundCount += 1
    nextChoice = (randomChoice + 1) % 3
    print "nextChoice: " + str(nextChoice)
    output = ["R","P","S"][nextChoice]