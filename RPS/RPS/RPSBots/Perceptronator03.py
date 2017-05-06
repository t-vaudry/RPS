##########################
#   Perceptronator! 0.3  #
##########################
# Uses perceptrons to predict your moves#

#Changes:
# 0.2: Removed punishment
# 0.3: Reduced move history to 3

import random

#Beat a move
def Beat(move):
    if move=="R":
        output="P"
    if move=="P":
        output="S"
    if move=="S":
        output="R"

def Train(network, reward, hist):
  if len(hist)==6:
    #First, "forget" the past...
    for x in xrange(6):
        for y in xrange(3):
            network[x][y]*=0.9
            
    #Now, the magic!
    for x in xrange(6):
        #for y in xrange(3):
        #        network[x][y]-=reward/2
        if hist[x]=="R":
            network[x][0]+=reward
        elif hist[x]=="P":
            network[x][1]+=reward
        elif hist[x]=="S":
            network[x][2]+=reward
            
def Eval(network, h):
  if len(h)==6:
    result=0.0
    for x in xrange(6):
        if h[x]=="R":
            result+=network[x][0]
        elif h[x]=="P":
            result+=network[x][1]
        elif h[x]=="S":
            result+=network[x][2]
    return result

class cfg:
    PredRock=PredPaper=PredSciss=[]
    history=[]

#Initialize
if input=="":
    
    #The history variable - holds last 3 moves, starts randomly
    #Format: me, them, me, them...
    for i in xrange(6):
        cfg.history+=random.choice(["R", "P", "S"])
    
    #The neural network weights - predicts next move (supposedly)
    #This is an implementation of a perceptron-like thing
        
        for a in xrange(6):
            for b in [cfg.PredRock, cfg.PredPaper, cfg.PredSciss]:
                b.append([0.0, 0.0, 0.0])
    #Just start with a random move
    output=cfg.history[4]

else:
    #Train the things
        if input=="R":
            Train(cfg.PredRock, 1, cfg.history)
            Train(cfg.PredPaper, -1, cfg.history)
            Train(cfg.PredSciss, -1, cfg.history)
        elif input=="P":
            Train(cfg.PredRock, -1, cfg.history)
            Train(cfg.PredPaper, 1, cfg.history)
            Train(cfg.PredSciss, -1, cfg.history)
        elif input=="S":
            Train(cfg.PredRock, -1, cfg.history)
            Train(cfg.PredPaper, -1, cfg.history)
            Train(cfg.PredSciss, 1, cfg.history)
            
    #Predict a move
        ro=Eval(cfg.PredRock, cfg.history)
        pa=Eval(cfg.PredPaper, cfg.history)
        sc=Eval(cfg.PredSciss, cfg.history)
        if ro>pa:
            pred=ro
        else:
            pred=pa
        if pred<sc:
            pred=sc
        cfg.history+=output
        
        if pred==ro:
            Beat("R")
        elif pred==pa:
            Beat("P")
        else:
            Beat("S")

    #Manage history
        cfg.history+=input
        cfg.history.pop(0)
        cfg.history.pop(0)