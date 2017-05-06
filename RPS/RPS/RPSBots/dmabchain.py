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
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
        table = {}
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        mem= 4
        M = 1
        delta = 0.01
        lda = 15
        
        state = [0]*(M*3)
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hi = [pa]
        hit = states[yo]+states[tu]
        prognosis = [random.choice(st) for i in range(M*3)]
        choices = []
        total = 0

        times = [1,1,1]
        reward = [0,0,0]
        upperconf=[0,0,0]
        m_=[0,0,0]
        M_=[0,0,0]


    else:
          tu = sdic[input]
          pa = (yo,tu)
          hi += [pa] #length(hi) == N

          
          
      
          r = res[yo][tu]
          total = total + r
          times[myprog] += 1.0
          reward[myprog] += (res[yo][tu]+1)/2.0

          upperconf = [(reward[i])/(times[i]) + math.sqrt((2.0*math.log(N))/times[i])  for i in range(M*3)]

          i = myprog
          m_[i] += reward[i]/times[i] + delta - (res[yo][tu]+1)/2.0
          M_[i] = max([m_[i], M_[i]])
          if (M_[i] > m_[i] + lda):
                times = [1,1,1]
                reward = [0,0,0]
                upperconf=[0,0,0]
                m_=[0,0,0]
                M_=[0,0,0]
     
          

    count = [[0,0,0],[0,0,0]]
    if (N > mem + 1):
        
        p = hi[N-mem-2:N-1]
        
        s = hi[N-1]

        key0 = p
        for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
            k = tuple(key+[s])
            if (k in table): table[k] += 1 
            else: table[k]= 1

        p = hi[N-mem-1:N]
        for y in st:
            for t in st:
                key0 = p
                for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
                    k = tuple(key+[(y,t)])
                    if (k in table):
                         z = table[k]
                         count[0][y] += z
                         count[1][t] += z

    prognosis[0] = best([count[1][i] for i in st])
    
    for j in range(1):
        prognosis[j*3 + 1] = (prognosis[j*3] + 1) % 3
        prognosis[j*3 + 2] = (prognosis[j*3+1] + 1) % 3


    myprog = highest(upperconf)
    yo = prognosis[myprog]
    
        
    output = states[yo]  
        
    N = N + 1