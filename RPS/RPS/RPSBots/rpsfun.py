import random

choices = ["R", "P", "S"]
global rState 
rState = choices
global pState
pState = choices
global sState 
sState = choices
global cState
cState = ""

def addLastPlay(input):
    if cState == "R":
        rState.append(input)
    elif cState == "P":
        pState.append(input)
    elif cState == "S":
        sState.append(input)

def getNewState(input):
    cState = input
    if cState == "R":
        return rState
    elif cState == "P":
        return pState
    elif cState == "S":
        return sState
    else:
        return choices
        
def chooseThrow(state):
    guess = random.choice(state)
    if guess == "R":
        return "P"
    elif guess == "P":
        return "S"
    elif guess == "S":
        return "R"

def main(input):
    addLastPlay(input)
    state = getNewState(input)
    output = chooseThrow(state)
    return output
    
output = main(input)