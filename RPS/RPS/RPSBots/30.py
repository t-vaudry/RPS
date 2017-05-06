import random
from collections import defaultdict


class Igralec:
    ime = "Jure Slak"

    def __init__(self): 
        self.history = ""
        self.my_history = ""
        self.win = {'K': 'P', 'P': 'S', 'S': 'K'}
        self.lose = {'K': 'S', 'P': 'K', 'S': 'P'}
        self.maxlen = 50000

    def poteza(self, rez, pr):
        if pr == ('X','X'):
            return random.choice(['K','P','S'])
    
        self.my_history += pr[0]
        self.history += pr[1]
        if len(self.my_history) > self.maxlen:
            self.my_history = self.my_history[1:]
            self.history = self.history[1:]                                                                                                                                        
                                                                                                                                                                                   
        h = zip(self.my_history, self.history)                                                                                                                                     
        i = 0; c = defaultdict(int)                                                                                                                                                
        i = h.index(pr, i)                                                                                                                                                         
        while i != len(h)-1:                                                                                                                                                       
            c[h[i+1][1]] += (1 << i)                                                                                                                                               
            i = h.index(pr, i+1)                                                                                                                                                   
                                                                                                                                                                                   
#        print c                                                                                                                                                                   
                                                                                                                                                                                   
        if len(c) == 0: # not found in history                                                                                                                                     
            choice = random.choice(['K','P','S'])                                                                                                                                  
        else:                                                                                                                                                                      
            choice = self.win[max(c, key=lambda x: c[x])]                                                                                                                          
                                                                                                                                                                                   
        return choice                                                                                                                                                              

leg = {'K':'R','P':'P','S':'S'}
i = Igralec()
if input == '':
    prev = i.poteza((0,0),('X','X'))
    output = leg[prev]
else:
    prev = i.poteza((0,0),(prev,input))
    output = leg[prev]