#autoregress.py continually learns from opponent using autoregression.

import random

def tochar(x):
    return {
        1: "R",
        2: "P",
        3: "S"
    }[x]

if input == "":
    #initialize variables, coefficients, and tables.
    n = 10
    alpha = .1
    Radj = 1
    Padj = 1
    Sadj = 1
    Hist = []
    Num = []
    Rval = []
    Pval = []
    Sval = []
    last = ""
    for i in range(n):
        Rval.append([random.random(), random.random(), random.random(), random.random(), random.random(), random.random()])
        Pval.append([random.random(), random.random(), random.random(), random.random(), random.random(), random.random()])
        Sval.append([random.random(), random.random(), random.random(), random.random(), random.random(), random.random()])
    win = {"P": "S", "S": "R", "R": "P"}
    split = {"RR": [1, 0, 0, 1, 0, 0], "RP": [1, 0, 0, 0, 1, 0], "RS": [1, 0, 0, 0, 0, 1], "PR": [0, 1, 0, 1, 0, 0], "PP": [0, 1, 0, 0, 1, 0], "PS": [0, 1, 0, 0, 0, 1], "SR": [0, 0, 1, 1, 0, 0], "SP": [0, 0, 1, 0, 1, 0], "SS": [0, 0, 1, 0, 0, 1], "R": [0, 0, 0, 1, 0, 0], "P": [0, 0, 0, 0, 1, 0], "S": [0, 0, 0, 0, 0, 1]}

if len(Hist) < n:
    response = tochar(random.randint(1,3))
    Hist.append(input + response)
    output = response

elif len(Hist) == n:
    #code history numerically.
    Num = []
    for val in Hist:
        Num.append(split[val])
    
    #adjust coefficients using input
    if input == "R":
        Radj = 1
        Padj = 0
        Sadj = 0
    elif input == "P":
        Radj = 0
        Padj = 1
        Sadj = 0
    elif input == "S":
        Radj = 0
        Padj = 0
        Sadj = 1
    for i in range(n):
        for j in range(6):                                                              
            (Rval[i])[j] = (Rval[i])[j] + (alpha * (Num[i])[j] * (Radj - (Rval[i])[j]))
            (Pval[i])[j] = (Pval[i])[j] + (alpha * (Num[i])[j] * (Padj - (Pval[i])[j]))
            (Sval[i])[j] = (Sval[i])[j] + (alpha * (Num[i])[j] * (Sadj - (Sval[i])[j]))
    #predict next value and submit win[value]
    Rraw = 0
    Praw = 0
    Sraw = 0
    #update history and code numerically.
    Hist.append(input + last)
    Hist.pop(0)
    Num = []
    for val in Hist:
        Num.append(split[val])
    for k in range(n):
        for l in range(6):
            Rraw = Rraw + (Num[k])[l] * (Rval[k])[l]
            Praw = Praw + (Num[k])[l] * (Pval[k])[l]
            Sraw = Sraw + (Num[k])[l] * (Sval[k])[l]
    if Rraw > Praw and Rraw > Sraw:
        response = win["R"]           
        output = response
        last = response
    elif Praw > Sraw:
        response = win["P"]  
        output = response
        last = response
    else:
        response = win["S"]
        output = response
        last = response