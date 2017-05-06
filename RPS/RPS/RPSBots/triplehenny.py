#triple henny, c.f. henny from Johannes Fuernkranz http://webdocs.cs.ualberta.ca/~darse/rsbpc.html

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
        states = ["R","S","P"]
        st = [0,1,2]
        sdic = {"R":0, "S":1, "P":2}

        yo = random.choice(st)
        tu = random.choice(st)

        hi = [tu]


    else:
          tu = sdic[input]
          hi += [tu]
  


    prob = [0,0,0]
    # triplehenny
    for j in range(3):
        prob[(hi[random.choice(range(N))])]+=1
    yo = (best(prob)) 
    #yo = (highest(prob)+2) % 3
    output = states[yo]  
        
    N = N + 1