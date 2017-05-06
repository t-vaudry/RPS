import math
# HATES MONKEEEEEYYSSS D:<
# and Anakin Skywalker D:<

if not input:
    prob = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    olast = 0
    ilast = 0
    monkeyhate = 0
else:
    ilast = {'R':0, 'P':1, 'S':2}[input]
    ind = 6*oprev + 2*iprev
    prob[ind] *= 0.95
    prob[ind+1] *= 0.95
    if olast < 2:
        prob[ind+olast] += 0.05
    monkeyhate *= 0.95
    monkeyhate += (4+omonkey-ilast)%3 - 1
ind = 6*olast + 2*ilast
rateR = math.exp(5*(1-prob[ind]-2*prob[ind+1]))
rateP = math.exp(5*(2*prob[ind]+prob[ind+1]-1))
rateS = math.exp(5*(prob[ind+1]-prob[ind]))

if rateS-rateP > rateR-rateS and rateS-rateP > rateP-rateR:
    omonkey = "R"
elif rateR-rateS > rateP-rateR:
    omonkey = "P"
else:
    omonkey = "S"
if monkeyhate >= 0:
    output = omonkey
else:
    output = {'R':'P', 'P':'S', 'S':'R'}[input]
oprev = olast
iprev = ilast
olast = {'R':0, 'P':1, 'S':2}[output]
omonkey = {'R':0, 'P':1, 'S':2}[omonkey]