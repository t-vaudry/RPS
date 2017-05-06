import random

def sampwprob(p):
    r = random.random()
    if (r < p[0]): return 1
    elif (r < p[0]+p[1]): return 2
    else: return 3

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

if(1):
    if (input == ""):
        N = 1
        mem = 4
        AR1 = 0.8
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = [{},{}]
        fade = 0.01      
        result = ["-","=","+"]
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        models = [1,1,1, 1,1,1, 1,1,1, 1,1,1, 0,0,0, 1,1,1]
        M = 6
        state = [0] * (M*3)
        yo= random.choice(st)
        tu = random.choice(st)
        hi1 = [yo]
        hi2 = [tu]
        prognosis = [random.choice(st) for i in range(M*3)]
        choices = []

    else:
          tu = sdic[input]
          hi1.append(yo)
          hi2.append(tu)
  
          state = [ AR1 * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3)]

          r = res[yo][tu]
          total = total + r
  

    count =  [[0]* 3]* 3
    
    if (N > mem + 1):
        
        p = [hi1[N-mem-1:N-1], hi2[N-mem-1:N-1]]
        s = [hi1[N-mem-2], hi2[N-mem-2]]
        ins = [0,0]
        for i in [0,1]:
            ins[i] = tuple([s[1]]+ p[i])
            if (ins[i] in table[i]): table[i][ins[i]] += 1+N*fade
            else: table[i][ins[i]]= 1+N*fade
            
            for j in st:
                if (tuple([j]+ p[i]) in table[i]): count[i][j] = table[i][tuple([j]+p[i])]
      
    prognosis[0] = highest([-c for c in count[0]]) #least freq me
    prognosis[3] = highest(count[0]) #highest freq me
    prognosis[6] = highest([-c for c in count[1]]) #least freq you
    prognosis[9] = highest(count[1]) #highest freq you


  
 
    # modelrandom
    prognosis[3*(M-1)] = random.choice(st)
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3


    best = highest(state)
    choices += [best]
    yo = prognosis[best]
    
    output = states[yo]  
    N = N + 1