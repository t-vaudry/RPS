import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

    


if (1):
    if (input == ""):
        N = 1
        cutoff = 400
        AR1 = 0.80
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        decay = 0.0
        decay2 = 0.5
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        M = 4
        models = [1]*(M*3+1)
        
        state = [1]*(M*3+1)
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        prognosis = [random.choice(st) for i in range(M*3+1)]
        choices = []


    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]

          state = [ AR1 * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3+1)]

          r = res[yo][tu]
          total = total + r
          
    if 1:
        count =  [[0]* 3]* 6
        for pos in range(max(3, cutoff), N-1):
              if (hi[pos-1] == hi[N-2] and hi[pos] == hi[N-1]):
                  count[0][hi[pos-2][0]] += 1 + pos * decay
                  count[1][hi[pos-2][1]] += 1 + pos * decay
              if (hi[pos-1][0] == hi[N-2][0] and hi[pos-1][0] == hi[N-1][0]):
                  count[2][hi[pos-2][0]] += 1 + pos * decay
                  count[3][hi[pos-2][1]] += 1 + pos * decay
              if (hi[pos-1][1] == hi[N-2][1] and hi[pos-1][1] == hi[N-1][1]):
                  count[4][hi[pos-2][0]] += 1 + pos * decay
                  count[5][hi[pos-2][1]] += 1 + pos * decay
             

  

    prognosis[0] = (lowest([count[1][i] + count[3][i] + count[5][i] for i in range(3)]) +1) % 3
    prognosis[3] = (highest([count[0][i] + count[2][i] + count[4][i] for i in range(3)]) +1) % 3
    prognosis[6] = (highest([count[1][i] + count[3][i] + count[5][i] for i in range(3)]) +1) % 3
    prognosis[9] = (lowest([count[0][i] + count[2][i] + count[4][i] for i in range(3)]) +1) % 3
    
    # modelrandom
    prognosis[3*M] = (random.choice(hi)[1] + 2) % 3
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3

    thebest = highest(state)
  
    choices += [thebest]
    
    yo = prognosis[thebest]
    
    output = states[yo]  
        
    N = N + 1