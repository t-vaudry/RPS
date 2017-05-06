import random

def full_search(subsetSize, maxDist, myHistory, theirHistory):
    myRecent=myHistory[len(myHistory)-subsetSize:]
    theirRecent=theirHistory[len(theirHistory)-subsetSize:]
    for i in range(len(myHistory)-subsetSize-1, max(len(myHistory)-maxDist, 0), -1):
        if myHistory[i:i+subsetSize]==myRecent and theirHistory[i:i+subsetSize]==theirRecent:
            return theirHistory[i+subsetSize]

    return []

def partial_search(subsetSize, maxDist, history):
    recent=history[len(history)-subsetSize:]
    for i in range(len(history)-subsetSize-1, max(len(myHistory)-maxDist, 0), -1):
        if history[i:i+subsetSize]==recent:
            return history[i+subsetSize]

    return []

if input=='':
    myHistory=[]
    theirHistory=[]
    options=['R','P','S']
    beats={'R':'P', 'P':'S', 'S':'R'}

    lastState=-1
    scores=[10,10]

else:
    if beats[input]==myHistory[len(myHistory)-1]:# win
        scores[lastState]=(scores[lastState]*19+1.)/20
    else:
        scores[lastState]=scores[lastState]*19/20.
        
    theirHistory.append(input)
    
if random.random()<.6:
    lastState=0
    for i in range(12,2,-1):
        temp=full_search(i, 150, myHistory, theirHistory)
        if len(temp):
            break
else:
    lastState=1
    for i in range(12,1,-1):
        temp=partial_search(i, 120, myHistory)
        if len(temp):
            temp=beats[temp]
            break

if len(temp)==0:
    output=random.sample(options, 1)[0]
else:
    output=beats[temp]

myHistory.append(output)