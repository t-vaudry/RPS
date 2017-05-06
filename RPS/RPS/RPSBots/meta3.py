""" Use multiple top strategies from the leaderboard and select
the one that is performing the best historically.

benjamin.haley@gmail.com Aug 2012

borrowed stragies from:
    pyfex (http://www.rpscontest.com/entry/135001)
    dllu (http://www.rpscontest.com/entry/338001)
"""

import random

class s1:
    def __init__(self):
      self.hist = ""
      self.opp_played = []
      self.beat = {'P': 'S', 'S': 'R', 'R': 'P'}
      self.beat2 = {'PP': 'S', 'SS': 'R', 'RR':'P', 'PS': 'S', 'PR': 'P', 'RS': 'R', 'RP': 'P', 'SP': 'S', 'SR': 'R'}
      self.complement = {'PS': 'R', 'PR': 'S', 'RS': 'P', 'RP': 'S', 'SP': 'R', 'SR': 'P'}
      
      self.score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
      self.output = random.choice(["R", "P", "S"])

      self.candidates1 = [self.output, self.output]
      self.candidates2 = [self.output] * 5
      self.performance1 = [0, 0]
      self.performance2 = [(0,0)] * 5

    def predict(self, input):
      self.hist += self.output.lower()+input
      self.opp_played.append(input)
      self.performance1[0] += self.score[self.candidates1[0]+input]
      self.performance1[1] += self.score[self.candidates1[1]+input]
      
      for i, p in enumerate(self.candidates2):
        self.performance2[i] = ({1:self.performance2[i][0]+1, 0: self.performance2[i][0], -1: 0}[self.score[p+input]],  
                       self.performance2[i][1]+self.score[p+input])

      index1 = self.performance1.index(max(self.performance1))
      index2 = self.performance2.index(max(self.performance2, key=lambda x: x[0]**3+x[1]))
      self.candidates1[1] = self.beat[random.choice(self.opp_played)]
      
      for length in range(min(10, len(self.hist)-2), 0, -2):
        search = self.hist[-length:]
        idx = self.hist.rfind(search, 0, -2)
        if idx != -1:
          my = self.hist[idx+length].upper()
          opp = self.hist[idx+length+1]
          self.candidates2[0] = self.beat[opp]
          self.candidates2[1] = self.beat[self.beat[my]]
          self.candidates2[2] = self.beat2[self.beat[my] + self.beat[self.beat[opp]]]
          self.candidates2[3] = self.beat2[self.beat[opp] + self.beat[self.beat[my]]]
          self.candidates2[4] = self.complement[''.join(sorted(set(self.candidates2[0] + self.candidates2[1] + self.candidates2[3])))]
          break
      else:
          candidates = [random.choice(['R', 'P', 'S'])] * 5
     
      self.candidates1[0] = self.candidates2[index2]
      
      self.output = self.candidates1[index1]
      return self.output

class s2:
    def __init__(self):
        self.numPre = 18
        self.numMeta = 6
        self.limit = 8
        self.beat={'R':'P','P':'S','S':'R'}
        self.moves=['','','']
        self.pScore=[[3]*self.numPre,[3]*self.numPre,[3]*self.numPre,[3]*self.numPre,[3]*self.numPre,[3]*self.numPre]
        self.centrifuge={'RP':'a','PS':'b','SR':'c','PR':'d','SP':'e','RS':'f','RR':'g','PP':'h','SS':'i'}
        self.length=0
        self.p=[random.choice("RPS")]*self.numPre
        self.m=[random.choice("RPS")]*self.numMeta
        self.mScore=[3]*self.numMeta
        self.output = random.choice('RPS')
        
    def predict(self, input):
        for i in range(self.numPre):
                self.pScore[0][i]=0.8*self.pScore[0][i]+((input==self.p[i])-(input==self.beat[self.beat[self.p[i]]]))*3
                self.pScore[1][i]=0.8*self.pScore[1][i]+((self.output==self.p[i])-(self.output==self.beat[self.beat[self.p[i]]]))*3
                self.pScore[2][i]=0.87*self.pScore[2][i]+(input==self.p[i])*3.3-(input==self.beat[self.p[i]])*0.9-(input==self.beat[self.beat[self.p[i]]])*3
                self.pScore[3][i]=0.87*self.pScore[3][i]+(self.output==self.p[i])*3.3-(self.output==self.beat[self.p[i]])*0.9-(self.output==self.beat[self.beat[self.p[i]]])*3
                self.pScore[4][i]=(self.pScore[4][i]+(input==self.p[i])*3)*(1-(input==self.beat[self.beat[self.p[i]]]))
                self.pScore[5][i]=(self.pScore[5][i]+(self.output==self.p[i])*3)*(1-(self.output==self.beat[self.beat[self.p[i]]]))
        for i in range(self.numMeta):
                self.mScore[i]=(self.mScore[i]+(input==self.m[i]))*(1-(input==self.beat[self.beat[self.m[i]]]))
        self.moves[0]+=self.centrifuge[input+self.output]
        self.moves[1]+=input		
        self.moves[2]+=self.output
        self.length+=1
        for y in range(3):
                j=min([self.length,self.limit])
                while j>=1 and not self.moves[y][self.length-j:self.length] in self.moves[y][0:self.length-1]:
                        j-=1
                i = self.moves[y].rfind(self.moves[y][self.length-j:self.length],0,self.length-1)
                self.p[0+2*y] = self.moves[1][j+i] 
                self.p[1+2*y] = self.beat[self.moves[2][j+i]] 
        
        for i in range(6,6*3):
                self.p[i]=self.beat[self.beat[self.p[i-6]]]
                
        for i in range(0,6,2):
                self.m[i]=       self.p[self.pScore[i  ].index(max(self.pScore[i  ]))]
                self.m[i+1]=self.beat[self.p[self.pScore[i+1].index(max(self.pScore[i+1]))]]
        self.output = self.beat[self.m[self.mScore.index(max(self.mScore))]]
        if max(self.mScore)<0.07 or random.randint(3,40)>self.length:
                self.output=self.beat[random.choice("RPS")]
        

if input == '':
    history = ''
    s1_ns = {}
    s2_ns = {}
    record = {'s1':0, 's2':0}
    values = {
        'RR':  0,
        'RP':  1,
        'RS': -1,
        'PR': -1,
        'PP':  0,
        'PS':  1,
        'SR':  1,
        'SP': -1,
        'SS':  0,
    }
    s1_ = s1()
    s2_ = s2()

else:
    history += input
    record['s1'] += values[input + s1_guess]
    record['s2'] += values[input + s2_guess]
    s1_.predict(input)
    s2_.predict(input)

if len(history) % 7 == 0:
    record['s1'] = 0
    record['s2'] = 0   

s1_guess = s1_.output
s2_guess = s2_.output
output = s1_guess if record['s1'] >= record['s2'] else s2_guess
print record, s1_guess, s2_guess, output, s1_guess == s2_guess