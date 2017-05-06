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
    learningfactor = 0.7
    played=[0,0,0]
else:
    for i in range(numpatterns):
        if input == patterns[i]:
            patterncount[i]+= 1
#print 'computer played ratio'
#print patterncount
patternsum = sum(patterncount)
for i in range(numpatterns):
    #if patterns are available:
    #p(i)=
    if patternsum > 0:
        learnedprobabilities[i]=learningfactor*patterncount[i]/patternsum+(1-learningfactor)*baseprobabilities[i]
    else:
        learnedprobabilities[i]=baseprobabilities[i]
#print 'predicted ratio'
#print learnedprobabilities
output = beat[weighted_choice([("R",learnedprobabilities[0]),("P",learnedprobabilities[1]),("S",learnedprobabilities[2])])]
#if output == patterns[0]:
#    played[0]+=1
#elif output == patterns[1]:
#    played[1]+=1
#elif output == patterns[2]:
#    played[2]+=1
#cntratio=[0,0,0,0]
#cntratio[0]=played[0]/float(1000)     
#cntratio[1]=played[1]/float(1000)
#cntratio[2]=played[2]/float(1000)
#print 'mybot played ratio'
#print cntratio