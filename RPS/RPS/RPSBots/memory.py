import random

def search(subsetSize, maxDist, myHistory, theirHistory):
    myRecent=myHistory[len(myHistory)-subsetSize:]
    theirRecent=theirHistory[len(theirHistory)-subsetSize:]
    for i in range(len(myHistory)-subsetSize-1, max(len(myHistory)-maxDist, 0), -1):
        if myHistory[i:i+subsetSize]==myRecent and theirHistory[i:i+subsetSize]==theirRecent:
            return theirHistory[i+subsetSize]

    return []

if input=='':
    myHistory=[]
    theirHistory=[]
    options=['R','P','S']
    beats={'R':'P', 'P':'S', 'S':'R'}

else:
    theirHistory.append(input)
    
for i in range(12,1,-1):
    temp=search(i, 120, myHistory, theirHistory)
    if len(temp):
        break

if len(temp)==0:
    output=random.sample(options, 1)[0]
else:
    output=beats[temp]

myHistory.append(output)