import math
import random

if input == "": # initialize variables for the first round
    totalCntr = 1.0
    rewardR = rewardP = rewardS = 0.0
    rockOutCntr = paperOutCntr = scissorsOutCntr = 1.0
else:
    totalCntr += 1


if ((input == "R") and (output == "R")):
    rewardR += 0.5
elif ((input == "P") and (output == "P")):
    rewardP += 0.5
elif ((input == "S") and (output == "S")):
    rewardS += 0.5
elif ((input == "R") and (output == "S")):
    rewardR += 1.0
elif ((input == "P") and (output == "R")):
    rewardP += 1.0
elif ((input == "S") and (output == "P")):
    rewardS += 1.0

xR = rewardR / totalCntr
xP = rewardP / totalCntr
xS = rewardS / totalCntr

ucbR = xR + math.sqrt(2 * math.log(totalCntr) / rockOutCntr)
ucbP = xP + math.sqrt(2 * math.log(totalCntr) / paperOutCntr)
ucbS = xS + math.sqrt(2 * math.log(totalCntr) / scissorsOutCntr)


ucblist = [ucbR, ucbP, ucbS]
maxv = float("-inf")
chlist = []
for i in range(3):
    if (ucblist[i] > maxv):
        maxv = ucblist[i]
        chlist = [i]
    elif (ucblist[i] == maxv):
        chlist.append(i)

outval = random.choice(chlist);

if (outval == 0):
    output = "R"
    rockOutCntr += 1.0
elif (outval == 1):
    output = "P"
    paperOutCntr += 1.0
else:
    output = "S"
    scissorsOutCntr += 1.0