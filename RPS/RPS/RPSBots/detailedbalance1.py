import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def notlowest(v):
    return random.choice([i for i in range(len(v)) if (min(v) != v[i]) or (max(v) == v[i])])
#input=""
if(1):

    if (input == ""):
        N = 1
        mem = 4
        AR1 = 0.83
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = {}
        fade = .01
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        M = 2
        #models = [1]*(M*3+1)
        models = [1]*6 + [1] 
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
        
        key0 = hi[N-mem-1:N-1]
        s = hi[N-mem-2]

        for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
            k = tuple([s] + key) # sic!
            if (k in table): table[k] += 1+N*fade
            else: table[k]= 1+N*fade

        for y in st:
            for t in st:
                k = tuple([(y,t)] + key0)
                if (k in table):
                    z = table[k]
                    count[0][y] += z
                    count[1][t] += z
                 
                for key in [[(i[0],-1) for i in key0], [(-1,i[1]) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table):
                         z = table[k]
                         count[0][y] += z*0.3
                         count[1][t] += z*0.3
    prognosis[0] = highest(count[0]) #highest freq me
    prognosis[3] = highest(count[1]) #highest freq you
    
    if(random.choice([0,1])):        
        prognosis[0] = notlowest(count[0]) #highest freq me
    if(random.choice([0,1])):        
        prognosis[3] = notlowest(count[1]) #highest freq you
    
        #prognosis[0] = highest([-c for c in count[0]]) #not lowest freq me
        #prognosis[3] = highest([-c for c in count[1]]) #not lowest freq you
  
 
    # modelrandom
    prognosis[3*M] = random.choice(st)
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3


    best = highest(state) #no random fallback
    choices += [best]
    yo = prognosis[best]
    
    output = states[yo]  
        
    N = N + 1
#print(total)