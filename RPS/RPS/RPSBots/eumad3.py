import random

def scoring(out):
    reward = 0
    if ((input == "R") and (out == "R")):
        reward += 0.5
    elif ((input == "P") and (out == "P")):
        reward += 0.5
    elif ((input == "S") and (out == "S")):
        reward += 0.5
    elif ((input == "R") and (out == "P")):
        reward += 1.0
    elif ((input == "P") and (out == "S")):
        reward += 1.0
    elif ((input == "S") and (out == "R")):
        reward += 1.0
    return reward



if (input == ""):
    test = ""
    rewards = [0,0,0,0,0,0,0,0]
    scoreRot0 = 0
    scoreRot1 = 0
    scoreRot2 = 0
    scoreRndm = 0
    scoreAlwaysR = 0
    scoreAlwaysP = 0
    scoreAlwaysS = 0
    outHSM = random.choice(['R', 'P', 'S'])
    rewards[0] = scoreHSM = 0
else:
    test += input
    scoreHSM += scoring(outHSM)
    rewards[0] = scoreHSM
    for length in range(min(5, len(test)-1), 0, -1):
        trova = test[-length:]
        pos = test.rfind(trova, 0, (len(test) - length))
        if (pos == -1):
            outHSM = random.choice(['R', 'P', 'S'])
        else:
            if (test[pos+length] == "R"):
                outHSM = "P"
            elif (test[pos+length] == "S"):
                outHSM = "R"
            else:
                outHSM = "S"



if not input:
    outRot0 = random.choice(['R', 'P', 'S'])
    rewards[1] = scoreRot0 = 0
else:
    outRot0 = {'R':'R', 'P':'P', 'S':'S'}[input]
    scoreRot0 += scoring(outRot0)
    rewards[1] = scoreRot0


if not input:
    outRot1 = random.choice(['R', 'P', 'S'])
    rewards[2] = scoreRot1 = 0
else:
    outRot1 = {'R':'P', 'P':'S', 'S':'R'}[input]
    scoreRot1 += scoring(outRot1)
    rewards[2] = scoreRot1


if not input:
    outRot2 = random.choice(['R', 'P', 'S'])
    rewards[3] = scoreRot2 = 0
else:
    outRot2 = {'R':'S', 'P':'R', 'S':'P'}[input]
    scoreRot2 += scoring(outRot2)
    rewards[3] = scoreRot2


outRndm = random.choice(['R', 'P', 'S'])
scoreRndm += scoring(outRndm)
rewards[4] = scoreRndm


outAlwaysR = 'R'
scoreAlwaysR += scoring(outAlwaysR)
rewards[5] = scoreAlwaysR


outAlwaysP = 'P'
scoreAlwaysP += scoring(outAlwaysP)
rewards[6] = scoreAlwaysP


outAlwaysS = 'S'
scoreAlwaysS += scoring(outAlwaysS)
rewards[7] = scoreAlwaysS

max = 0
maxIndex = 0
for i in range(len(rewards)):
    if rewards[i] > max:
        max = rewards[i]
        maxIndex = i
if (maxIndex == 0):
    output = outHSM
elif (maxIndex == 1):
    output = outRot0
elif (maxIndex == 2):
    output = outRot1
elif (maxIndex == 3):
    output = outRot2
elif (maxIndex == 4):
    output = outRndm
elif (maxIndex == 5):
    output = outAlwaysR
elif (maxIndex == 6):
    output = outAlwaysP
elif (maxIndex == 7):
    output = outAlwaysS