import random

if input=="":
    beats={'R':'P', 'P':'S', 'S':'R'}
    last=random.sample(['R','P','S'],1)[0]
    myLast=''
    state=random.randint(0,2)

    score=0
    longScore=0
    roundNum=0

else:
    last=input

    if roundNum>200 and (longScore*1./roundNum)<-1+.08*roundNum/100:
        state=-1
    else:
        if beats[myLast]==last:
            score-=1
            longScore-=1
        if beats[last]==myLast:
            score+=1
            longScore-=1

        if score<=0 and roundNum%5==0:
            state=(state+1)%3
            score=0

        roundNum+=1
    
if state==0:
    temp=last
elif state==1:
    temp=beats[last]
elif state==2:
    temp=beats[beats[last]]
else:
    temp=random.sample(['R','P','S'],1)[0]

myLast=temp
output=temp