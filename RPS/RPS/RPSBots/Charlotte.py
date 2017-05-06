'''
Date: 04.05.13
Bot: Charlotte
Author: Patron

Dedicated to Charlotte Gainsbourg '''

import random
from operator import itemgetter
from heapq import nlargest

rchoice = random.choice

def MyCounter (xs):
    ''' Count elelments in a list.
        Smaller analogue of collections.Counter in python 2.7+ '''
    result = {}
    for x in xs:
        if x not in result.keys():
            result[x] = 1
        else: result [x] += 1
    return result
def MyMostCommon (xdict, n=2):
    ''' List the n most common elements and their counts from the most
        common to the least.
        Smaller analogue of method most_common in Counter. '''
    return nlargest(n, xdict.iteritems(), key=itemgetter(1))

class Core:
    def __init__ (self):
        self.freq = {'R': 0, 'P': 0, 'S': 0}
    
    def shift_by (self, move, k = 1):
        return X[(X.index(move)+k)%3]

    global X, merge, split
    X = ['R','P','S']
    # a is input, b is output
    merge = dict([(a+b,str(X.index(a)*3+X.index(b))) for a in X for b in X])
    split = dict([(str(X.index(a)*3+X.index(b)),a+b) for a in X for b in X])

    ### Basic Strategies ###
    def _History (self, history, option=0):
        ''' Return hero move based on history match.
            Option = 1 defines counter algorithm. '''
        for l in range(min(len(history)-1, 15), 2, -1):
            part = history[-l:]
            idx = history.rfind(part,0,-1)
            if idx != -1:
                next_move = split[history[idx+l]][option]
                return self.shift_by(next_move)
        else: return rchoice(X)

    def _Frequency (self, history, option=0):
        ''' Return hero move based on most common opponent move. '''
        last_opp_move = split[history[-1]][0]
        self.freq[last_opp_move] += 1
        next_move = max(self.freq, key = self.freq.get)
        return self.shift_by(next_move)
    
    def _Rotation (self, history, option=0):
        ''' Return hero move based on last opponent move. '''
        return self.shift_by(split[history[-1]][option])

    ### Metastrategies ###
    def Guessing (self, history, strategy, option=0):
        ''' Straightforward implementation of 'strategy'. '''
        move_by_strategy = strategy(self, history, option)
        return move_by_strategy
    def doubleGuessing (self, history, strategy, option=0):
        ''' If opponent anticipates we use 'strategy'. '''
        move_by_strategy = strategy(self, history, option)
        return self.shift_by(move_by_strategy, k=2)
    def tripleGuessing (self, history, strategy, option=0):
        ''' If opponent anticipates we use double guessing. '''
        move_by_strategy = strategy(self, history, option)
        return self.shift_by(move_by_strategy, k=1)

    ### All strategies ###
    strategies = {0: _History, 1: _Frequency, 2: _Rotation}
    
    def metastrategies (self, history, num_of_strategy):
        ''' For each strategy build metastrategy. '''
        i, j = num_of_strategy//6, num_of_strategy%6
        if j == 0: return self.Guessing(history, self.strategies[i])
        elif j == 1: return self.doubleGuessing(history, self.strategies[i])
        elif j == 2: return self.tripleGuessing(history, self.strategies[i])
        elif j == 3: return self.Guessing(history, self.strategies[i], 1)
        elif j == 4: return self.doubleGuessing(history, self.strategies[i], 1)
        elif j == 5: return self.tripleGuessing(history, self.strategies[i], 1)

class Charlotte (Core):
    def __init__(self):
        Core.__init__(self)
        self.history = ''
        self.mode = 'defense'
        self.score = 0
        self.out = rchoice(X)
        self.accuracy = dict([(i,0) for i in range(len(self.strategies)*6)])
        self.selection = 'naive'
        
    ### Mode selection. ###
    def modeSelection (self):
        if len(self.history) < 5:
            self.mode = 'defense'
        elif self.score < -5:
            self.mode = 'attack'
        elif self.score > 5:
            self.mode = 'defense'
        else: self.mode = 'normal'

    ### Strategy selection ###
    def naiveSelection (self):
        ''' Choose strategy with best accuracy by naive method. '''
        return max(self.accuracy, key = self.accuracy.get)

    def decayedSelection (self, d = .9):
        for s in self.accuracy:
            self.accuracy[s] *= d
                    
    ### Accuracy ###
    price = {'RP':1, 'PS':1, 'SR': 1,
             'RR':0, 'PP':0, 'SS':0,
             'RS':-1, 'PR':-1, 'SP':-1}
    
    def updateAcc (self, history):
        ''' Update accuracy for each strategy. '''
        if len(history) > 1:
            last_opp_move = split[history[-1]][0]
            for N in range(len(self.strategies)*6):
                self.accuracy[N] += self.price[
                    last_opp_move + self.metastrategies(history[:-1], N)]
            if self.selection == 'decayed':
                self.decayedSelection()

    ### Move selection ###
    def moveSelection (self):
        ''' Decide what to do next with respect to tactic. '''            
        if self.mode == 'defense':
            return rchoice(X)
        elif self.mode == 'normal':
            strategy = self.naiveSelection()
            return self.metastrategies(self.history, strategy)
        elif self.mode == 'attack':
            strategy = self.naiveSelection()
            move = self.metastrategies(self.history, strategy)
            all_moves = []
            for N in range(len(self.strategies)*6):
                all_moves.append(self.metastrategies(self.history, N))
            top_two_moves = MyMostCommon(MyCounter(all_moves))
            if top_two_moves[0][0] != move:
                return top_two_moves[0][0]
            else: return top_two_moves[1][0]

    ### Next move ###
    def nextMove (self, inp, selection = 'naive'):
        if selection == 'decayed': self.selection = 'decayed'
        if inp:
            self.history += merge[inp+self.out]
            self.score += self.price[inp+self.out]
            self.updateAcc(self.history)
            self.modeSelection()
            self.out = self.moveSelection()
            #print self.history, self.score, self.mode, self.out
        return self.out

charlotte = Charlotte()
output = charlotte.nextMove(input)