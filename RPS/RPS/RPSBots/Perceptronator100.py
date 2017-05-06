##########################################
#           Perceptronator! 1.00         #
##########################################
# Uses perceptrons to predict your moves #
##########################################
# Changes:
# 1.0: Changed reward to cubed instead of squared

import random
class cfg:
    #2 * moves to remember
    Moves=10
    
    try:
        print PredRock
    except:
        PredRock=PredPaper=PredSciss=[]
        #The neural network weights - predicts next move (supposedly)
        #This is an implementation of a perceptron-like thing
        
        for a in xrange(Moves):
            for b in [PredRock, PredPaper, PredSciss]:
                b.append([0.0, 0.0, 0.0])
    
    try:
        print history
    except:
        #The history variable - holds last cfg.Moves/2 moves, starts randomly
        #Format: me, them, me, them...
        history=["R","R","P","S","R","P","S","R","S","S"]
pos=["R", "P", "S"]
    

#Beat a move
def Beat(move):
    output=pos[(pos.index(move)+1)%3]

def Train(network, reward, hist):
  if len(hist)==cfg.Moves:
    #First, "forget" the past...
    for x in xrange(cfg.Moves):
        for y in xrange(3):
            network[x][y]*=0.95
            
    #Now, the magic!
    for x in xrange(cfg.Moves):
        value=reward*((x+1.0)/cfg.Moves)**3
        #Punish the other weights
        for y in xrange(3):
                network[x][y]-=2*value
        #Remove punishment and add the value to the winning weight        
        network[x][pos.index(hist[x])]+=3*value
           
def Eval(network, h):
  if len(h)==cfg.Moves:
    result=0.0
    for x in xrange(cfg.Moves):
		result+=network[x][pos.index(h[x])]
    return result

#Initialize
if input=="":
    #Just start with a random move
    output=random.choice(pos)
else:
    #Train the things
        if input=="R":
            Train(cfg.PredRock, 1.0, cfg.history)
            Train(cfg.PredPaper, -1.0, cfg.history)
            Train(cfg.PredSciss, -1.0, cfg.history)
        elif input=="P":
            Train(cfg.PredRock, -1.0, cfg.history)
            Train(cfg.PredPaper, 1.0, cfg.history)
            Train(cfg.PredSciss, -1.0, cfg.history)
        elif input=="S":
            Train(cfg.PredRock, -1.0, cfg.history)
            Train(cfg.PredPaper, -1.0, cfg.history)
            Train(cfg.PredSciss, 1.0, cfg.history)
            
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
    #Beat it!
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