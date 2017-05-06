import random

def highest(v):
    return random.choice([i for i in range(3) if max(v) == v[i]])

if(1):
    if (input == ""):
        N = 1
        states = ["R","S","P"]
        sdic = {"R":0, "S":1, "P":2}
        result = ["-","=","+"]
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        total=0
        r=0
        move = 0
        last =  random.choice([1,2,3])
        print(N, states[last-1])

    else:
        lastrow = r
        r = res[sdic[output]][sdic[input]]
        total = total + r
        state[lastrow-1][move-1] += r
        

    move = highest(state[r+1])-1
    if (N < 50 or random.choice(range(10))== 0): move = random.choice([1,2,3])
    last = (last + move) % 3 + 1
    output = states[last-1] 
    N = N + 1