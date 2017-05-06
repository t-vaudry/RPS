import random

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
                   

def metric(hi, n,m):
    countn = [[0,0,0],[0,0,0]]
    countm = [[0,0,0],[0,0,0]]
    def decay(i): return 1/(i+1.0)
    w = sum([decay(i) for i in range(7)])
  
    h1 = h2 = h3 = 1
    for i in range(min(n,m, 15)):
        
        if h1 and hi[n-i] == hi[m-i]:
            w += decay(i)
        else:
            h1 = 0
        if h2 and hi[n-i][1] == hi[m-i][1]:
            w += decay(i)
        else:
            h2 = 0
        if h3 and hi[n-i][0] == hi[m-i][0]:
            w += decay(i)
        else:
            h3 = 0
    return w  
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
        AR1 = .85#0.85
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        forwardbias = 2
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        MEM1 = MEM2 = MEM3 = []
        
        MEM4 = [6]
    
        M1 = len(MEM1)*3
        M2 = len(MEM2)*2
        M3 = len(MEM3)
        M4 = len(MEM4)*3
        M = M1 + M2 + M3 + M4
        models = ([1,.7,.7]*M4)
      
        
        state = [0] * (M*3)
      
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        hiyt = states[yo]+states[tu]
        hit = states[yo]+" "
        hiy = " " + states[tu]
        prognosis = [random.choice(st) for i in range(M*3)]
        choices = []


    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa]

          hiyt += states[yo]+states[tu]
          hit += states[yo]+" "
          hiy += " " + states[tu]
          
          if (res[yo][tu] == 1):
              state = [state[i] + 1.5*(yo==prognosis[i]) for i in range(M*3)]
          else:    
              state = [state[i] + (1+res[prognosis[i]][tu]) * models[i] for i in range(M*3)]
 

    i = -3
    # Squad
    for h in MEM4:
        proby = [0.0,0.0,0.0]
        probt = [0.0,0.0,0.0]
        for j in range(h):
            k = max([random.choice(range(N)) for l in range(forwardbias)])
            m = metric(hi, k-1, N-1)
            proby[(hi[k][0])]+= m
            probt[(hi[k][1])]+= m
        i += 3; prognosis[i] = best([probt[l] +proby[(l+0)% 3] for l in st])
        i += 3; prognosis[i] = best([probt[l] +proby[(l+2)% 3] for l in st])
        i += 3; prognosis[i] = best([probt[l] +proby[(l+1)% 3] for l in st])
    
        #i += 3; prognosis[i] = (best(proby))
        #i += 3; prognosis[i] = (best(probt))

   


    i += 3; assert(i==3*M)


   
  
    for j in range(M1 + M2+M4):
        prognosis[j*3 + 1] = (prognosis[j*3] + 1) % 3
        prognosis[j*3 + 2] = (prognosis[j*3+1] + 1) % 3
    
    ms = min(state)
    state2 = [s - ms for s in state]

    b = weightedchoice(range(M*3), state2, 2)

    
    yo = prognosis[b]
   
    
    output = states[yo]  
        
    N = N + 1