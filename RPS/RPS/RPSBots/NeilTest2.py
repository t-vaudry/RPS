import random
output = random.choice(["R", "P", "S"])
HISTORY_L=2
def most_common(l):
    max = 0
    maxitem = None
    for x in set(l):
        count =  l.count(x)
        if count > max:
            max = count
            maxitem = x
    return maxitem

if input == "": # initialize variables for the first round
        history=''
        for n in range(1, HISTORY_L):
                history += random.choice(['R','P','S'])

history += input

guess=most_common(history[-HISTORY_L:-1])

if guess == "R":
	output = "S"
elif guess == "P":
	output = "R"
elif guess == "S":
	output = "P"