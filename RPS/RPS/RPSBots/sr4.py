import random, math
#db

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

def mean(c):
    return sum(c)/length(c)

# alpha in [0,1]: greediness 
def attack(yo, tu, alpha):
    r = res[yo][tu]
    p1 = yo
    if r == -1:
        p1 = (yo + 1) % 3
    elif r == 0 and random.random() < alpha:
        p1 = (yo + 2) % 3
    return p1
                   

if(1):
    if (input == ""):
        N = 1
        AR1 = .85#0.85
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        alpha = .1
        alpha2 = .1
        table = {}
        cutoff = 200
        fade = 0.01
        decay1 = 0.98
        decay2 = 0.5
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        MEM = [] # 3, 5
        MEM2 = [3,4,5]
        hennies = [10] # 10
    
        M1 = len(MEM)*3
        M2 = len(MEM2)*2
        M3 = len(hennies)*1
        M = M1 + M2 + M3
        models = [1,1,1,1,1,1,1,1,1]*0 + [1,1,1,.2,.2,.2,.2,.2,.2]*0 + [1,0.3,0.3]*(M2)+ [1,0.25,0.25]*M3 #[1,0.5,0.5] #[1]*(M*3+1)
        smodels =[ [0,0,0]*(M1)+ [1,0,0]*(M2)+ [1,0,0]*M3,
                   [0,0,0]*(M1)+[0,.3,0]*(M2)+ [0,.6,0]*M3,
                   [0,0,0]*(M1)+[0,0,.3]*(M2)+ [0,0,.6]*M3]
        smodelmask =[ [0,0,0]*(M1)+ [1,0,0]*(M2)+ [1,0,0]*M3,
                   [0,0,0]*(M1)+[0,1,0]*(M2)+ [0,1,0]*M3,
                   [0,0,0]*(M1)+[0,0,1]*(M2)+ [0,0,1]*M3]
      
        
        state = [0] * (M*3)
        substate = [0,0,0]
        
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        hiyt = states[yo]+states[tu]
        hit = states[yo]+" "
        hiy = " " + states[tu]
        prognosis = [random.choice(st) for i in range(M*3+1)]
        choices = []


    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]

          hiyt += states[yo]+states[tu]
          hit += states[yo]+" "
          hiy += " " + states[tu]
          state = [ AR1 * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3)]
          substate = [AR1 * substate[i] for i in range(len(substate))]
          for k in range(len(substate)):
              substate[k] += sum([res[prognosis[i]][tu] * smodels[k][i] for i in range(M*3)])
         
          r = res[yo][tu]
          total = total + r
  

    # Predictor: Backwards looking markov chain
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

    #Prectictor "Dalton board"    
    prop =  [random.choice(st) for j in range(len(MEM2)*2)]
    for m in MEM2:
      if(N > m):
        key = hiyt[-2*m:]
        pos = N*2 - m*2
   
        if (random.random() < decay1):
   
          while 1:
            pos = hiyt.rfind(key,(int(N/2))*2,pos)
            if pos > 1:
                prop[i] = sdic[hiyt[pos + 2*m]]
                prop[i+1] = sdic[hiyt[pos + 2*m+1]]
            
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
       i += 3; prognosis[i] = (prop[m]+2) % 3 # attack myself
       i += 3; prognosis[i] = (prop[m+1]+2) % 3
      # i += 3; prognosis[i] = attack(prop[m],prop[m+1], alpha)
      # i += 3; prognosis[i] = attack(prop[m],prop[m+1], 1-alpha)

    # Predictor: "squad of hennies"
    #if 0:
    for h in hennies:
      if h > 1:
        prob = [0,0,0]
        for j in range(h):
            k = max(random.choice(range(N)),random.choice(range(N)))
            prob[(hi[k][1])]+=1
        i += 3; prognosis[i] = (best(prob))
      else:
        k = max(random.choice(range(N)),random.choice(range(N)))
        p1 = attack(hi[k][0], hi[k][1], alpha2)
        p2 = (hi[k][1] + 2) % 3
        i += 3; prognosis[i] = p1
        #i += 3; prognosis[i] = p2
   

    i += 3; assert(i==3*M)


   
  
    for j in range(M):
        prognosis[j*3 + 1] = (prognosis[j*3] + 1) % 3
        prognosis[j*3 + 2] = (prognosis[j*3+1] + 1) % 3


    s = highest(substate)
    #best = highest([state[k]*smodelmask[s][k] for k in range(M*3)])
    best = highest(state)   
    yo = prognosis[best]

    
    output = states[yo]  
        
    N = N + 1