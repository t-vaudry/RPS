import random

count = 0
if input == "":
    output = random.choice(["R","P","S"])
    count +=1
else:
    if(count%2==0):
        output = random.choice(["R","P","S"])
        count+=1
    else:
        output = output
        count+=1