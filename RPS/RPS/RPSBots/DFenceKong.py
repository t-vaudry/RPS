import math
import random
# loves primates
# and will protect the helpless ones

if not input:
    prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    olast = 0
    ilast = 0
else:
    ilast = {'R':0, 'P':1, 'S':2}[input]
    ind = 6*oprev + 2*iprev
    prob[ind] *= 0.95
    prob[ind+1] *= 0.95
    if ilast < 2:
        prob[ind+ilast] += 0.05
ind = 6*olast + 2*ilast
rateR = math.exp(5*(1-prob[ind]-2*prob[ind+1]))
rateP = math.exp(5*(2*prob[ind]+prob[ind+1]-1))
rateS = math.exp(5*(prob[ind+1]-prob[ind]))
randNum = random.random()*(rateR+rateP+rateS)

if randNum < rateR:
    output = "S"
elif randNum < rateR+rateP:
    output = "R"
else:
    output = "P"
oprev = olast
iprev = ilast
olast = {'R':0, 'P':1, 'S':2}[output]