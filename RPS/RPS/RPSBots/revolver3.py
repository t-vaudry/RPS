import random

def sampwprob(p):
    r = random.random()
    if (r < p[0]): return 1
    elif (r < p[0]+p[1]): return 2
    else: return 3
if(1):
    if (input == ""):
        N = 1
        AR1 = 0.95
        hist = []
        states = ["R","S","P"]
        sdic = {"R":0, "S":1, "P":2}
        result = ["-","=","+"]
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        statew = [0, 0, 0]
        statel = [0,0,0]
        total=0
        r=0
        move = 0
        last =  random.choice([1,2,3])
    else:
        lastr = r
        r = res[sdic[output]][sdic[input]]
        total = total + r
        statew = [s*AR1 for s in statew]
        statel = [s*AR1 for s in statel]

        if(lastr == 1): statew[move-1] += r
        elif (lastr == -1): statel[move-1] -= r

    if(random.choice([2])==1): v = statel
    else: v = statew

    if (r == -1): v = [max(v) - s  + 1 for s in v]
    elif (r == 0): v = [1,1,1]
    elif (r == 1): v = [s - min(v) + 1 for s in v]
    
    v = [s/sum(v) for s in v]
    
    move = sampwprob(v)
   

    last = (last + move) % 3 + 1
        
        
    output = states[last-1] 
    N = N + 1