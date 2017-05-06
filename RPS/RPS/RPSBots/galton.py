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
        hennies = 5
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        r=0
        MEM2 = [3,4,5]
        M = len(MEM2)*2 + 1
       
        models = [.3,.3,1]*(len(MEM2)*2)+ [1,0.6,0.6]
        state = [0] * (M*3)
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
          state = [ AR1 * state[i] + res[prognosis[i]][tu] * models[i] for i in range(M*3)]

          r = res[yo][tu]
  	


    i = 0

    
    prop =  [random.choice(st) for j in range(len(MEM2)*2)]
    for m in MEM2:
      if(N + 1> m):
        key = tuple(hi[-m-1:-1])
        if (key in table): 
        	table[key] += [pa]
        else: 
	        table[key] = [pa]
      if(N > m):
        key = tuple(hi[-m:])

	if (key in table): 
	  	ch = table[key]
	  	k = len(ch)
	  	k = max(random.choice(range(0,k)),random.choice(range(0,k)))
	  	

	        prop[i] = ch[k][0]
                prop[i+1] = ch[k][1]

      i += 2
     
    i = -3;
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