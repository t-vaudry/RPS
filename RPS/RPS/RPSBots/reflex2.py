import random

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

    

                   
if(1):
    if (input == ""):
        N = 1
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}
    
        yo = random.choice(st)
        tu = random.choice(st)

        pa = (yo, tu)
        hit = [tu]
    
    else:
          tu = sdic[input]
          hit += [tu]

    p = [0,0,0]
    #1.) hit against random move
    p[hit[random.randint(0, N-1)]] += 1
    p[hit[random.randint(0, N-1)]] += 1
    p[hit[random.randint(0, N-1)]] += 1
    
    #2.) the same, but only if it worked before
    a1 = random.randint(0, N-1)
    a2 = random.randint(0, N-1)
    i = min(a1, a2)
    j = max(a1, a2)
    x = random.randint(0, N-1)
  
    p[(3 + hit[x] + (hit[j] - hit[i]))%3] += 1
    
                

    #3.) if you try to beat 1.), you will have to repeat yourself
    if N > 100:
      h = random.randint(1, 3) #lag
      j = random.randint(h+1, N-h)
      p[(3+ hit[N-h] + hit[j]- hit[j-h])%3] += 1
    
    

    yo  =  best(p)
    
    output = states[yo]  
        
    N = N + 1