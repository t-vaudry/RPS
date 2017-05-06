#different fade
import random

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
        table = [0,0,0,0,{},{}]

        fade = 0.01 
        decay2 = 0.5
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        total=0
        r=0
        M = 8
        models = [1]*(M*3+1)
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
  

    count = [0,0,0,0,[[0,0,0],[0,0,0]],[[0,0,0],[0,0,0]]]
    for mem in [4,5]:
      if (N > mem + 1):
        
        p = hi[N-mem-1:N-1]
        
        s = hi[N-mem-2]

        key0 = p
        for key in [key0, [(i[0],-1) for i in key0], [ (-1,i[1]) for i in key0]]:
            k = tuple([s] + key)
            if (k in table[mem]): table[mem][k] += 1+N*fade
            else: table[mem][k]= 1+N*fade

        for y in st:
            for t in st:
                key0 = p
                for key in [key0, [(i[0],-1) for i in key0], [(-1,i[1]) for i in key0]]:
                    k = tuple([(y,t)] + key)
                    if (k in table[mem]):
                         z = table[mem][k]
                         count[mem][0][y] += z
                         count[mem][1][t] += z
    
    count4 = [[count[4][0][i] + count[4][1][(i+0)% 3] for i in st]]
    count4 += [[count[4][0][i] + count[4][1][(i+1)% 3] for i in st]]
    count4 += [[count[4][0][i] + count[4][1][(i+2)% 3] for i in st]]
    count5 = [[count[5][0][i] + count[5][1][(i+0)% 3] for i in st]]
    count5 += [[count[5][0][i] + count[5][1][(i+1)% 3] for i in st]]
    count5 += [[count[5][0][i] + count[5][1][(i+2)% 3] for i in st]]


    prop =  [random.choice(st) for i in range(6)]
    for pos in range(N-1,max(3, N-200),-1):
              if (hi[pos-1] == hi[N-2] and hi[pos] == hi[N-1]):
                  prop[0] = hi[pos-2][0]
                  if (random.random() < decay2): break
    for pos in range(N-1,max(3, N-200),-1):
              if (hi[pos-1][1] == hi[N-2][1] and hi[pos][1] == hi[N-1][1]):
                  prop[5] = hi[pos-2][1]
                  if (random.random() < decay2): break    

    i = 0;  prognosis[i] = best(count4[0])
    i += 3; prognosis[i] = best(count4[1])
    i += 3; prognosis[i] = best(count4[2])
    i += 3; prognosis[i] = best(count5[0])
    i += 3; prognosis[i] = best(count5[1])
    i += 3; prognosis[i] = best(count5[2])
    i += 3; prognosis[i] = prop[0]
    i += 3; prognosis[i] = prop[5]
  
    assert(i+3==3*M)

 
    # modelrandom
    prognosis[3*M] = random.choice(st)
    
  
    for i in range(M):
      prognosis[i*3 + 1] = (prognosis[i*3] + 1) % 3
      prognosis[i*3 + 2] = (prognosis[i*3+1] + 1) % 3


    best = highest(state)
    choices += [best]
    yo = prognosis[best]
    
    output = states[yo]  
        
    N = N + 1