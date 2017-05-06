import random

if(1):
    if (input == ""):
        states = ["R","S","P"]
        sdic = {"R":0, "S":1, "P":2}
        result = ["+","=","-"]
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        l = 0
        L = 0
        R = 0
    else:
        r = res[sdic[output]][sdic[input]]
        R = R + r
    if l >= L:
        if (R < 0 or input ==""):
            L = min(1+int(random.expovariate(.2)), 100)
            movev = [random.choice((-1,0,1)) for iii in range(0,L)]
            dstart = random.choice([1,0])
        R = 0
        l = 0
       
        if input=="" or dstart:
            state = movev[l]
        else:
            state = state + movev[l]
    else:
          state = state + movev[l]

    l = l + 1
    output = states[state % 3]