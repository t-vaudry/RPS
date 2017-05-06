import random

def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

if input == "": # initialize variables for the first round
    numpatterns=3    
    patterns=['R','P','S']
    patterncount=[0,0,0]
    beat={'R':'P','P':'S','S':'R'}
    bp=1/float(3)
    baseprobabilities=[bp,bp,bp]
    learnedprobabilities=[0,0,0]
    learningfactor = 0.3
else:
    for i in range(numpatterns):
        if input == patterns[i]:
            patterncount[i]+= 1

patternsum = sum(patterncount)
for i in range(numpatterns):
    #if patterns are available:
    #p(i)=
    if patternsum > 0:
        learnedprobabilities[i]=learningfactor*patterncount[i]/patternsum+(1-learningfactor)*baseprobabilities[i]
    else:
        learnedprobabilities[i]=baseprobabilities[i]
output = weighted_choice([("R",learnedprobabilities[0]),("P",learnedprobabilities[1]),("S",learnedprobabilities[2])])