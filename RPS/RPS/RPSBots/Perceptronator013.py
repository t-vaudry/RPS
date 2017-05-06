##########################################
#           Perceptronator! 0.13         #
##########################################
# Uses perceptrons to predict your moves #
##########################################
# Changes:
# 0.2:  Removed punishment
# 0.3:  Reduced move history to 3
# 0.4:  Increased move history to 10
# 0.5:  Attempts to remember learned values from previous games
#       Gives more importance to recent moves
#       Fixed bug (moves remembered were 0)
# 0.s:  Inverse-squared the history importance
# 0.6:  Increased moves history to 100
#       Attempts to remember history of games (better than random)
# 0.7:  Added punishment back
# 0.8:  Reverted to linear history importance
# 0.9:  Disabled forgetting, fixed punishing bug
# 0.10: Realized improvement was because of randomness
#       Changed moves remembered to 2
# 0.1e: Experiment: switch to next move estimation <-- failed
# 0.11: Increased forgetting and moves, started with non-random history
# 0.12: Remember 8 moves, increased forgetting even more (to 75%)
# 0.13: Remember 20 moves, 15%, back to inverse square

import random

#Global vars:
class cfg:
    #2 * moves to remember
    Moves=20
    
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
        history=["R","R","P","S","R","P","S","R","S","S"]*2
    

#Beat a move
def Beat(move):
    if move=="R":
        output="P"
    if move=="P":
        output="S"
    if move=="S":
        output="R"

def Train(network, reward, hist):
  if len(hist)==cfg.Moves:
    #First, "forget" the past...
    for x in xrange(cfg.Moves):
        for y in xrange(3):
            network[x][y]*=0.15
            
    #Now, the magic!
    for x in xrange(cfg.Moves):
        value=reward*((x+1.0)/cfg.Moves)**2
        #Punish the other weights
        for y in xrange(3):
                network[x][y]-=reward/2.0
        if hist[x]=="R":
            network[x][0]+=value
        elif hist[x]=="P":
            network[x][1]+=value
        elif hist[x]=="S":
            network[x][2]+=value
            
def Eval(network, h):
  if len(h)==cfg.Moves:
    result=0.0
    for x in xrange(cfg.Moves):
        if h[x]=="R":
            result+=network[x][0]
        elif h[x]=="P":
            result+=network[x][1]
        elif h[x]=="S":
            result+=network[x][2]
    return result

#Initialize
if input=="":
    #Just start with a random move
    output=random.choice(["R", "P", "S"])

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