#This algorithm is an attempt to win at Rock Paper Scissors BLIND -- ie, without looking at my opponent's throws at all.
import random

def our_output(num):
    if num==0:
        return "R"
    elif num==1:
        return "P"
    elif num==2:
        return "S"

if input=="":
    ourlist=[1]
elif len(ourlist)<=20:
    ourlist.append(random.randrange(0,3))
else:
    randomizer=random.uniform(0,1)
    print randomizer
    if randomizer>=.25:
        ourlist.append(random.randrange(0,3))
    else: 
        ourlist1 = ourlist[-6:]
        mode = max(set(ourlist1), key=ourlist1.count)
        num = (mode+2)%3
        ourlist.append(num)

output=our_output(ourlist[-1])