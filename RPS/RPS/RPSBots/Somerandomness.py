import random

if input == "":
    no_random = random.randint(1,10)
    no_normal = 0
    co_rock = co_paper = co_scissors = 0
elif input == "P":
    co_paper += 1
elif input == "R":
    co_rock += 1
elif input == "S":
    co_scissors += 1
    
if no_random != 0:
    output = random.choice(["R", "P", "S"])
    no_random -= 1    
    if no_random == 0:
        no_normal = random.randint(1,10)
elif no_normal != 0:
    if co_rock > co_paper and co_rock > co_scissors:
        output = "P"
    elif co_paper > co_scissors:
        output = "S"
    else:
        output = "R"
    
    no_normal -= 1
    if no_normal == 0:
        no_random = random.randint(1,10)