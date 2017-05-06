import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

def sweet(c):
    c2 = [c[1]-c[2], c[2]-c[0], c[0]-c[1]]
    mc = min(c2)
    return [cc - mc for cc in c2]
    


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

def attackpa(pa, alpha):
    yo = pa[0]
    tu = pa[1]
    r = res[yo][tu]
    p1 = yo
    if r == -1:
        p1 = (yo + 1) % 3
    elif r == 0 and random.random() < alpha:
        p1 = (yo + 2) % 3
    return p1

def cumsum(iterable):
    iterable= iter(iterable)
    s= iterable.next()
    yield s
    for c in iterable:
        s= s+ c
        yield s
def weightedchoice(v, w, no):
    ww = sum(w)
    if (ww == 0): return random.choice(v)

    w = [(ws/ww)**no for ws in w]
    ww = sum(w)
   
    ra = ww*random.random()
    j = 0
    for i in cumsum(w):
       # print(r,i)
        if ra <= i: break
        j+= 1
    return v[j]
    

                   
if(1):
    if (input == ""):
        N = 1
        AR1 = .95#0.85
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        forwardbias = 2
        dna = [0,1,2,3,4,5,6,7,8]
        dnadic = {(0,0): 0,(1,0): 1,(2,0): 2,
                  (0,1): 3,(1,1): 4,(2,1): 5,
                  (0,2): 6,(1,2): 7,(2,2): 8}
        pairs = [(0,0),(1,0),(2,0), (0,1),(1,1),(2,1), (0,2),(1,2),(2,2)]
        
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        MEM1 = MEM2 = MEM3 = []
        
#        MEM4 = [(0,0.6),(0,0.3),(1,0.7),(1,0.3),(2,0.9),(12,1)]
        MEM4 = [(0,0.9),(1,0.9),(2,0.9),(3,0.9),(12,0.9)]
        M1 = len(MEM1)
        M2 = len(MEM2)
        M3 = len(MEM3)
        M4 = len(MEM4)*2
        M = M1 + M2 + M3 + M4
        models = ([1, 1, 1]*M)
      
        
        state = [0] * (M*3)
        bold = [0] * (M*3)
      
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        hiyt = states[yo]+states[tu]
        hit = states[yo]+" "
        hiy = " " + states[tu]
        prognosis = [random.choice(st) for i in range(M*3)]
        choices = []
        pyo = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] 
        ptu = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
 
    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]

          hiyt += states[yo]+states[tu]
          hit += states[yo]+" "
          hiy += " " + states[tu]

          #models = [ models[i] + 0.1*(yo==prognosis[i]) for i in range(M*3)]
      
          
          if (res[yo][tu] == 1):
              state = [state[i] + 1.5*(yo==prognosis[i]) for i in range(M*3)]
          else:    
              state = [state[i] + (1+res[prognosis[i]][tu]) * models[i] for i in range(M*3)]
          
    
    for hr in MEM4:
        h = hr[0]
        r = hr[1]
        if h == 0:
            pyo[0][yo] = pyo[0][yo]*r + 1
            ptu[0][tu] = ptu[0][tu]*r + 1
        elif h < N:
            z = (hi[N-h-1][0]-yo)%3
            pyo[h][z] = pyo[h][z]*r + 1

            z = (hi[N-h-1][1]-tu )%3
            ptu[h][z] = ptu[h][z]* r + 1

          
    i = -3
    # Squad
    prognosis = [random.choice(st) for l in range(M*3)]
    
    for hr in MEM4:
        h = hr[0]
        if h == 0:
           i += 3; prognosis[i] = best(ptu[h])
           i += 3; prognosis[i] = highest(pyo[h])
        else:
           i += 3; prognosis[i] = (tu + best(ptu[h])) % 3
           i += 3; prognosis[i] = (yo + highest(pyo[h])) % 3
            
        
        
   
    i += 3; 
   
  
    for j in range(M):
        prognosis[j*3 + 1] = (prognosis[j*3] + 1) % 3
        prognosis[j*3 + 2] = (prognosis[j*3+1] + 1) % 3

    ms = min(state)
    state2 = [s - ms for s in state]

    b = weightedchoice(range(M*3), state2, 2)

    
    yo = prognosis[b]
    
    
    output = states[yo]  
        
    N = N + 1