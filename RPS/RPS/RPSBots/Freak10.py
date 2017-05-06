"""
As weird as how this algorithm works, this is the intended algorithm, made so it qualify RPS terms.
Despite having a nice large amount of randomness, this is intended and expected that 
a nice portion of randomness (nice is relative, BTW) will
help this algorithm. So in other word. No, it's not random submission.
"""
"""
Program name: Rational Freak 1.0
"""
from random import randint
history=[]
count=[0,0,0]
rps=["R","P","S"]
loseStreak=0
poop=0
boom=0
if input=="":
    output=rps[randint(0,2)]
else:
    history.append(input)
    poop=len(history)
    if poop<5 or poop%50==0 :
        output=rps[randint(0,2)]
    else:
        count=[0,0,0]
    for x in range(0,poop-1):
        if (history[x]==history[poop-1]):
            count[rps.index(history[x+1])]+=1

    for x in range(1,poop-1):
        if (history[x]==history[poop-1])and(history[x-1]==history[poop-2]):
            count[rps.index(history[x+1])]+=1

    for x in range(2,poop-1):
        if (history[x]==history[poop-1])and(history[x-1]==history[poop-2])and(history[x-2]==history[poop-3]):
            count[rps.index(history[x+1])]+=1

    for x in range(3,poop-1):
        if (history[x]==history[poop-1])and(history[x-1]==history[poop-2])and(history[x-2]==history[poop-3])and(history[x-3]==history[poop-4]):
            count[rps.index(history[x+1])]+=1
    if count[0]>count[1] and count[0]>count[2]:
        output="P"
    elif count[1]>count[2]:
        output="S"
    elif count[2]<count[1]:
        output="R"
    else:
        output=rps[randint(0,2)]