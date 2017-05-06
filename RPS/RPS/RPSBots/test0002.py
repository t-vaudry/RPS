import random

if input == "":
    wins = 0
    loss = 0
    
    myprev = ""
    enemyp = ""

    phit = 0
    shit = 0
    rhit = 0

    rbias = 33
    pbias = 33
    sbias = 34

if input == "R":
    rhit = rhit+1
if input == "P":
    phit = phit+1
if input == "S":
    shit = shit+1

total = shit + phit + rhit + 1
rbias = phit / total
sbias = rhit / total
pbias = shit / total

roll = random.randint(0,100)

if roll < rbias:
    output = "R"
elif roll < rbias + pbias:
    output = "P"
else:
    output = "S"