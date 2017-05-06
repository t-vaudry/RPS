import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

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
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

        MEM = [(0,.9),(1,0.9),(2,0.9),(3,0.90),(4,0.90), (5,0.90), (12,0.90), (30,0.90)]
        M = len(MEM)*2
        
        state = [0] * (M*3)
      
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        pyo = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] 
        ptu = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
 
    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]
      
          if (res[yo][tu] == 1):
              state = [state[i] + 1.5*(yo==prognosis[i]) for i in range(M*3)]
          else:    
              state = [state[i] + (1+res[prognosis[i]][tu]) for i in range(M*3)]
          
    
    for m in range(len(MEM)):
        
        h = MEM[m][0]
        r = MEM[m][1]
        if h == 0:
            pyo[0][yo] = pyo[0][yo]*r + 1
            ptu[0][tu] = ptu[0][tu]*r + 1
        elif h < N:
            z = (hi[N-h-1][0]-yo)%3
            pyo[m][z] = pyo[m][z]*r + 1

            z = (hi[N-h-1][1]-tu )%3
            ptu[m][z] = ptu[m][z]* r + 1

          
    i = -3
    prognosis = [random.choice(st) for l in range(M*3)]
    
    for m in range(len(MEM)):
        
        h = MEM[m][0]
        if h == 0:
           i += 3; prognosis[i] = best(ptu[m])
           i += 3; prognosis[i] = highest(pyo[m])
        else:
           i += 3; prognosis[i] = (tu + best(ptu[m])) % 3
           i += 3; prognosis[i] = (yo + highest(pyo[m])) % 3
            
        
        
   
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