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
    p[hit[random.randint(0, N-1)]] += 1
    for k in [300,100]:
        if N > k: p[hit[random.randint(N-k-1, N-1)]] += 1
    

    j = random.randint(0, N-1)
    p[(3 + tu + hit[j]- hit[j-1])%3] += 1

   
    if N > 5:
     j = random.randint(5, N-1)
     p[(3+ hit[N-4] + hit[j]- hit[j-5])%3] += 1
    
    if N > 5:
     j = random.randint(5, N-1)
     p[(16+ sum(hit[N-5:N]) - sum(hit[j-5:j]))%3] += 1
  

    yo  =  best(p)
            
    
    output = states[yo]  
        
    N = N + 1