import random

def search(subsetSize, dist, history):
    recent=history[len(history)-subsetSize:]
    for i in range(len(history)-subsetSize-1, len(history)-subsetSize-dist, -1):
        if history[i:i+subsetSize]==recent:
            return history[i+subsetSize]

    return []

if input=='':
    history=[]
    options=['R','P','S']
    beats={'R':'P', 'P':'S', 'S':'R'}
    
    for i in range(50):
        history.append(random.sample(options, 1)[0])
    
for i in range(10,1,-1):
    temp=search(i, 40-i, history)
    if len(temp):
        break

if len(temp)==0:
    output=random.sample(options, 1)[0]
else:
    output=beats[beats[temp]]

history.append(output)