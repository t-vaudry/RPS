import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])


def notlowest(v):
    return random.choice([i for i in range(len(v)) if (min(v) != v[i]) or (max(v) == v[i])])
#input=""
#for III in range(5):
if(1):
    if input == "":
        N = 1
        mem = 4 #e.g. 4
        M = 4
        AR1 = [0.80]*3 + [0.85]*3 + [0.85]*3 + [0.85]*3 + [0.85]  #e.g. 0.80
        #AR1 = [0.8]* (M*3+1)
        states = ["R","S","P"]
        boltz = [0,0,0]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = {}
        fade =  [0.015,0.01,0.005]  #e.g. 0.008
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        res2 = [[-0.1, 1, -1], [-1, -0.1, 1], [1, -1, -0.1]]
        total=0
        r=0
       
        #models = [1]*(M*3+1)
        models = [1.3]*3 + [0.95]*3 + [0.95]*3 + [0.95]*3 + [0]
        
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

          state = [ AR1[i] * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3+1)]

          r = res[yo][tu]
          total = total + r
  

    count =  [[0]* 3]* 6
    
    if (N > mem + 1):
        
        key0 = hi[N-mem-1:N-1]
        s = hi[N-mem-2]
        

        for j in range(3):
            keys = [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]
                                                                    
            k = tuple([s] + keys[j]) # sic!
            if (k in table): table[k] += 1+N*fade[j]
            else: table[k]= 1+N*fade[j]
        
        for y in st:
            for t in st:
                k = tuple([(y,t)] + key0)
                if (k in table):
                    z = table[k]
                    count[0][y] += z # we are trapped
                    count[1][t] += z

                for key in [[(i[0],-1) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table):
                         z = table[k]
                         count[2][y] += z # that looks like me
                         count[3][t] += z

                for key in [[(-1,i[1]) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table):
                         z = table[k]
                         count[4][y] += z # that looks like you
                         count[5][t] += z



    prognosis[0] = highest(count[0]) #we, my typical move

    prognosis[3] = highest([-c for c in count[5]]) #we, your least typical

    prognosis[6] = highest(count[5]) #[-c for c in count[5]]) #you, your least typical move

    
 
    # modelrandom
    prognosis[3*M] = random.choice(st)

   
    # modelbolz
    boltz = [boltz[i]*0.95 for i in range(3)]
    if tu == 0:
        boltz[1] -= 1
        boltz[2] += 1
    elif tu == 1:
        boltz[2] -= 1
        boltz[0] += 1
    else:
        boltz[0] -= 1
        boltz[1] += 1
    prognosis[9] = (highest(boltz) + 2) % 3
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3 #meta
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3 #beat prognosis


    best = highest(state) 
    choices += [best]
    yo = prognosis[best]
    
    output = states[yo]  
        
    N = N + 1