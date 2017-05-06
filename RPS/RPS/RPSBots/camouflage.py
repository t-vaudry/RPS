import random

WIN = {"R":"P","P":"S","S":"R"}
LEN = 5
k=""

class Strategy:
  last = "R"
  score = 1
  def __init__(self,*args):
    pass
  def predict(self,inp):
    return self.last

class Randor (Strategy):
  def predict(self,inp):
    return random.choice(["P","R","S"])


class Weibull (Strategy):
  def predict(self,inp):
    B = ["R","P","S"]
    o = random.weibullvariate(5.2,3.14)
    return B[int(o)%3]
    
  

class Playback(Strategy):
  def predict(self,inp):
    l = self.last
    if not l:
      l = inp
    self.last = inp
    return WIN[l]


class Guesser(Strategy):
  buf = ["R","S","P"]
  def predict(self,inp):
    if not inp:
      return "P"
    else:
      self.buf.append(inp)
      o = random.choice(self.buf)
      return WIN[o]


output="P"

if not input:
  strategies = { 
    "weibull":Weibull(),
    "guesser":Guesser(),
    "random":Randor(),
    "playback":Playback()
  }
else:
  bv=0
  for s,strat in strategies.iteritems():
    if strat.last == WIN[input]:
      strat.score += 0.05
    if strat.score >= 0.01:
      strat.score -= 0.01
    strat.last = k
    k = strat.predict(input)
    if strat.score >= bv :
      output = k
      bv = strat.score