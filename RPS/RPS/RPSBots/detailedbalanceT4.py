import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])


if(1):
    if (input == ""):
        N = 1
        mem = 4
        AR1 = 0.9
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = {}
        fade = 0.001
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        M = 4
        models = [1]*(M*3+1)
        state = [0] * (M*3+1)
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
  

    count =  [[0]* 3]* 2
    
    if (N > mem + 1):
        
        p = hi[N-mem-1:N-1]
        
        s = hi[N-mem-2]

        key0 = p
        for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
            k = tuple([s] + key)
            if (k in table): table[k] += 1+N*fade
            else: table[k]= 1+N*fade

        for y in st:
            for t in st:
                key0 = p
                for key in [key0, [(i[0],-1) for i in key0], [(-1,i[1]) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table):
                         z = table[k]
                         count[0][y] += z
                         count[1][t] += z

            
    prognosis[0] = highest([-c for c in count[0]]) #least freq me
    prognosis[3] = highest(count[0]) #highest freq me
    prognosis[6] = highest([-c for c in count[1]]) #least freq you
    prognosis[9] = highest(count[1]) #highest freq you

  
 
    # modelrandom
    prognosis[3*M] = random.choice(st)
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3


    best = highest(state)
    choices += [best]
    yo = prognosis[best]
    
    output = states[yo]  
        
    N = N + 1