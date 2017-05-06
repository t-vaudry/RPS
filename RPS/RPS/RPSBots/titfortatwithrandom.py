import random
if input == "":
    count = 0
    output = random.choice(["R","P","S"])
else:
    if count % 5 == 0:
        output = random.choice(["R","P","S"])
        count = 0
    count = count + 1
    output = input