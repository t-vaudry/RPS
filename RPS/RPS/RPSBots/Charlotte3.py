'''
Date: 04.08.13 - 04.09
Bot: Charlotte
Author: Patron
e-mail: ivanovserg[put ninety here] at gmail.com

v2 Deconstruction of classes since they exceed 5 sec CPU limit.
A few adjustments to d, noise. Use of only History analysis.
It turns out function calls are also expensive.

v3 Fixed err with double/triple guessing
Added history matching based on separated history of opp or hero
Check for frequency (hero/opp) at the end (if > 4) wo meta
Noise and slow decaying

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

def MyCounter (xs):
    ''' Count elelments in a list.
        Similar to collections.Counter in python 2.7+ '''
    result = {}
    for x in xs:
        if x not in result.keys():
            result[x] = 1
        else: result[x] += 1
    return result
def MyMostCommon (xdict, n=3):
    ''' List the n most common elements and their counts from the most
        common to the least.
        Similar to method most_common in Counter. '''
    return nlargest(n, xdict.iteritems(), key=itemgetter(1))

if True:
    if not input:
        history = ''
        Opphistory = ''
        Herohistory = ''
        mode = 'defense'
        score = 0
        N = 2 # Number of metastrategies 
        Hbool = False
        Oppbool = False
        Herobool = False
        moves = dict([(i,'') for i in range(N*6)])
        accuracy = dict([(i,0) for i in range(N*6)])
        Oppfrequency = dict([(move,0) for move in X])
        Herofrequency = dict([(move,0) for move in X])
        out = rchoice(X)
    else:
        ### Update history and score ###
        history += merge[input+output]
        Opphistory += input
        Herohistory += output
        score += price[input+output]
        Oppfrequency[input] += 1
        Herofrequency[output] += 1
        noise = 'off'
        oppfreq = 'off'
        ### Update accuracy (with decay) ###
        if len(history) > 3:
            if Hbool:
                for i in range(6): # For combined History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
            if Oppbool:
                for i in range(6,6+3): # For Opp History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
            if Herobool:
                for i in range(6+3,6+6): # For Hero History
                    accuracy[i] *= .9
                    accuracy[i] += price[input+moves[i]]
                    accuracy[i] = round(accuracy[i],4)
        ### Choose mode ###
        if len(history) < 4 or score >= 10:
            mode = 'defense'
        elif score <= -5:
            mode = 'attack'
        else:
            mode = 'normal'
        ### Update moves ###
            # Based on history matching (hero and opp combined) #
        for l in range(min(len(history)-1,15), 0, -1):
            part = history[-l:]
            idx = history.rfind(part,0,-1)
            if idx != -1:
                Hbool = True
                moves[0] = shift_by(split[history[idx+l]][0])
                moves[1] = shift_by(split[history[idx+l]][0],3)
                moves[2] = shift_by(split[history[idx+l]][0],2)
                moves[3] = shift_by(split[history[idx+l]][1])
                moves[4] = shift_by(split[history[idx+l]][1],3)
                moves[5] = shift_by(split[history[idx+l]][1],2)
                break
        else:
            Hbool = False
            for i in range(6):
                moves[i] = rchoice(X)
            # Based on history matching (hero and opp moves separated) #
        for l in range(min(len(Opphistory)-1,15), 0, -1):
            part = Opphistory[-l:]
            idx = Opphistory.rfind(part,0,-1)
            if idx != -1:
                Oppbool = True
                moves[6+0] = shift_by(Opphistory[idx+l])
                moves[6+1] = shift_by(Opphistory[idx+l],3)
                moves[6+2] = shift_by(Opphistory[idx+l],2)
                break
        else:
            Oppbool = False
            for i in range(3):
                moves[6+i] = rchoice(X)
        for l in range(min(len(Opphistory)-1,15), 0, -1):
            part = Herohistory[-l:]
            idx = Herohistory.rfind(part,0,-1)
            if idx != -1:
                Herobool = True
                moves[6+3] = shift_by(Herohistory[idx+l])
                moves[6+4] = shift_by(Herohistory[idx+l],3)
                moves[6+5] = shift_by(Herohistory[idx+l],2)
                break
        else:
            Herobool = False
            for i in range(3,6):
                moves[6+i] = rchoice(X)
        ### Choose move ###
        if mode == 'defense':
            out = rchoice(X)
        elif mode == 'normal':
            k = max(accuracy, key = accuracy.get)
            out = moves[k]
        elif mode == 'attack':
            k = max(accuracy, key = accuracy.get)
            move = moves[k]
            out = rchoice([s for s in X if s != move])
        ### Noise ###
        if random.random() <= 0.1:
            noise = 'on'
            out = rchoice(X)
        ### Frequency analysis ###    
        if len(history) > 4:
            opp_top2 = MyMostCommon(Oppfrequency,2)
            opp_thresh = opp_top2[0][1]-opp_top2[1][1]
            hero_top2 = MyMostCommon(Herofrequency,2)
            hero_thresh = hero_top2[0][1]-hero_top2[1][1]
            if hero_thresh > 3:
                out = shift_by(hero_top2[0][0],2)
            if opp_thresh > 3:
                oppfreq = 'on'
                out = shift_by(opp_top2[0][0])
            
    output = out