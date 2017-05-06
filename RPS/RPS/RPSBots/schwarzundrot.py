import random, math

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

if(1):
    if (input == ""):
        N = 1
        AR1 = 0.85
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = {}
        cutoff = 400
        fade = 0.01
        decay1 = 0.98
        decay2 = 0.5
        hennies = 5
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        MEM = [] # 3, 5
        MEM2 = [3,4,5]
        M = len(MEM)*3 + len(MEM2)*2 + 1
        
        models = [1,1,1,1,1,1,1,1,1,1,1,1,.2,.2,.2,.2,.2,.2]*  len(MEM) + [.3,.3,1]*(len(MEM2)*2)+ [1,0.6,0.6]#[1,0.5,0.5] #[1]*(M*3+1)
        state = [0] * (M*3)
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        hit = states[yo]+states[tu]
        prognosis = [random.choice(st) for i in range(M*3+1)]
        choices = []


    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]

          hit += states[yo]+states[tu]
          state = [ AR1 * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3)]

          r = res[yo][tu]
          total = total + r
  

    count = [[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]
    for m in range(len(MEM)):
      mem = MEM[m]
      if (N > mem + 1):
        
        p = hi[N-mem-1:N-1]
        
        s = hi[N-mem-2]

        key0 = p
        for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
            k = tuple([s] + key)
            weight = 1+N*fade 
            if (k in table): table[k] = weight
            else: table[k]= weight
       
        for y in st:
            for t in st:
                key0 = p
                for key in [key0, [(i[0],-1) for i in key0], [(-1,i[1]) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table):
                         z = table[k]
                         count[m][0][y] += z
                         count[m][1][t] += z
                         
    countagg = [[],[],[],[],[],[],[],[],[]]
    for  m in range(len(MEM)):
       countagg[m] = [[count[m][0][i] + count[m][1][(i+0)% 3] for i in st]]
       countagg[m] += [[count[m][0][i] + count[m][1][(i+1)% 3] for i in st]]
       countagg[m] += [[count[m][0][i] + count[m][1][(i+2)% 3] for i in st]]
    i = 0

    
    prop =  [random.choice(st) for j in range(len(MEM2)*2)]
    for m in MEM2:
      if(N > m):
        key = hit[-2*m:]
        pos = N*2 - m*2
        #prop[i] = sdic[hit[pos-1]] 
        #prop[i+1] = sdic[hit[pos-2]]

        if (random.random() < decay1):
          #prop[i] = (best(prob) + 1) % 3
          #prop[i+1] = (best(prob)+2) % 3
   
          while 1:
            pos = hit.rfind(key,max(0, N-cutoff),pos)
            if pos > 1:
               # prop[i] = sdic[hit[pos-1]]
               # prop[i+1] = sdic[hit[pos-2]]
                prop[i] = sdic[hit[pos + 2*m]]
                prop[i+1] = sdic[hit[pos + 2*m+1]]
            
            else:
                break
            if (random.random() < decay2): break
      i += 2
     
    i = -3;
    for m in range(len(MEM)):
       i += 3; prognosis[i] = best(countagg[m][0])
       i += 3; prognosis[i] = best(countagg[m][1])
       i += 3; prognosis[i] = best(countagg[m][2])

    for m in range(len(MEM2)):
       i += 3; prognosis[i] = (prop[m])
       i += 3; prognosis[i] = (prop[m+1])

    prob = [0,0,0]
    # triplehenny
    for j in range(hennies):
        prob[(hi[random.choice(range(max(0,N-cutoff),N))][1])]+=1
    i += 3; prognosis[i] = (best(prob))
    i += 3

    assert(i==3*M)


   
  
    for j in range(M):
        prognosis[j*3 + 1] = (prognosis[j*3] + 1) % 3
        prognosis[j*3 + 2] = (prognosis[j*3+1] + 1) % 3


    best = highest(state)
    yo = prognosis[best]


    
    output = states[yo]  
        
    N = N + 1