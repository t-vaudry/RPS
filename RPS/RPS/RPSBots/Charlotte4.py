'''
Date: 04.10.13 
Bot: Charlotte
Author: Patron
e-mail: ivanovserg9[put ninety here] at gmail.com

v4 Metastrategies now include only 3 types of strategies
since other 3 just repeat them.
Added rotation method
Consecutive loses switch mode to random
Switch to random every 75 rounds for 65 rounds (experimental)
For now the goal is to play randomly good vs serious bots
and reasonably good vs weak bots. Therefore it plays
randomly most of time with some switches to metas.

Dedicated to Charlotte Gainsbourg '''
import random
from operator import itemgetter
from heapq import nlargest
rchoice = random.choice

X = ['R','P','S']
merge = dict([(a+b,str(X.index(a)*3+X.index(b))) for a in X for b in X])
split = dict([(str(X.index(a)*3+X.index(b)),a+b) for a in X for b in X])
price = {'RP':1, 'PS':1, 'SR': 1,
        'RR':0, 'PP':0, 'SS':0,
        'RS':-1, 'PR':-1, 'SP':-1}

def shift_by (move, k = 1):
    return X[(X.index(move)+k)%3]
def gradient_of (history, k = 5):
    ''' Check balance of wins/loses for k last rounds. '''
    if len(history) < k:
        return 0
    else:
        part = history[-k:]
        gradient = [price[split[r]] for r in part]
        if sum(gradient) > 0: return 1
        elif sum(gradient) < 0: return -1
        else: return 0
def decline (gradient, k = 5):
    ''' Check whether it's decline of gradient '''
    if len(gradient) >= k:
        for b in gradient[-k:]:
            if b != -1:
                return False
        else: return True
    else: return False

if True:
    if not input:
        history = ''
        Opphistory = ''
        Herohistory = ''
        mode = 'defense'
        score = 0
        N = 8 # Number of metastrategies 
        Hbool = False
        Oppbool = False
        Herobool = False
        moves = dict([(i,rchoice(X)) for i in range(N*3)])
        accuracy = dict([(i,0) for i in range(N*3)])
        Oppfrequency = dict([(move,0) for move in X])
        Herofrequency = dict([(move,0) for move in X])
        gradient = []
        out = rchoice(X)
    else:
        ### Update history and score ###
        history += merge[input+output]
        Opphistory += input
        Herohistory += output
        score += price[input+output]
        gradient.append(gradient_of(history))
        Oppfrequency[input] += 1
        Herofrequency[output] += 1
        noise = 'off'
        ### Update accuracy ###
        if len(history) > 3:
            if Hbool:
                for i in range(6): # For combined History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
            if Oppbool:
                for i in range(6,9): # For Opp History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
            if Herobool:
                for i in range(9,12): # For Hero History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
            for i in range(12,18): # For rotation
                accuracy[i] *= .9
                accuracy[i] += price[input+moves[i]]
                accuracy[i] = round(accuracy[i],4)
            for i in range(18,24):
                accuracy[i] += 1*price[input+moves[i]]
                accuracy[i] = round(accuracy[i],4)
        ### Update mode ###
        if len(history)%75 < 65 or decline(history):
            mode = 'defense'
        else:
            mode = 'attack'
        ### Update moves ###
            # Based on history matching (combined) #
        for l in range(min(len(history)-1,15), 0, -1):
            part = history[-l:]
            idx = history.rfind(part,0,-1)
            if idx != -1:
                Hbool = True
                moves[0] = shift_by(split[history[idx+l]][0],1)
                moves[1] = shift_by(split[history[idx+l]][0],2)
                moves[2] = shift_by(split[history[idx+l]][0],3)
                moves[3] = shift_by(split[history[idx+l]][1],1)
                moves[4] = shift_by(split[history[idx+l]][1],2)
                moves[5] = shift_by(split[history[idx+l]][1],3)
                break
        else:
            Hbool = False
            for i in range(6):
                moves[i] = rchoice(X)
            # Based on history matching (opp history) #
        for l in range(min(len(Opphistory)-1,15), 0, -1):
            part = Opphistory[-l:]
            idx = Opphistory.rfind(part,0,-1)
            if idx != -1:
                Oppbool = True
                moves[6+0] = shift_by(Opphistory[idx+l],1)
                moves[6+1] = shift_by(Opphistory[idx+l],2)
                moves[6+2] = shift_by(Opphistory[idx+l],3)
                break
        else:
            Oppbool = False
            for i in range(3):
                moves[6+i] = rchoice(X)
            # Based on history matching (hero history) #
        for l in range(min(len(Herohistory)-1,15), 0, -1):
            part = Herohistory[-l:]
            idx = Herohistory.rfind(part,0,-1)
            if idx != -1:
                Herobool = True
                moves[9+0] = shift_by(Herohistory[idx+l],1)
                moves[9+1] = shift_by(Herohistory[idx+l],2)
                moves[9+2] = shift_by(Herohistory[idx+l],3)
                break
        else:
            Herobool = False
            for i in range(3):
                moves[9+i] = rchoice(X)
            # Based on rotation (opponent) #
        moves[12+0] = shift_by(input,1)
        moves[12+1] = shift_by(input,2)
        moves[12+2] = shift_by(input,3)
            # Based on rotation (hero) #
        moves[15+0] = shift_by(output,1)
        moves[15+1] = shift_by(output,2)
        moves[15+2] = shift_by(output,3)
            # Based on frequency (opponent) #
        opp_freq_move = max(Oppfrequency, key=Oppfrequency.get)
        moves[18+0] = shift_by(opp_freq_move,1)
        moves[18+1] = shift_by(opp_freq_move,2)
        moves[18+2] = shift_by(opp_freq_move,3)
            # Based on frequency (hero) #
        hero_freq_move = max(Herofrequency, key=Herofrequency.get)
        moves[21+0] = shift_by(hero_freq_move,1)
        moves[21+1] = shift_by(hero_freq_move,2)
        moves[21+2] = shift_by(hero_freq_move,3)
        ### Choose move ###
        if mode == 'defense':
            out = rchoice(X)
        elif mode == 'attack':
            k = max(accuracy, key = accuracy.get)
            #k = 3*(len(history)//10%8) #change meta instantly
            out = moves[k]
        ### Noise ###
        if random.random() <= 0.05:
            #print 'Noise'
            noise = 'on'
            out = rchoice(X)

    output = out