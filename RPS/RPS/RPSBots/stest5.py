import random

nf=1

if input == "": 
    lm = [1] * 27
    nf = 0
    e = m = [0,0,0]
else:
    if input == "R":
        ea = 0
    elif input == "P":
        ea = 1
    elif input == "S":
        ea = 2
     
    e+=[ea]

if nf:

    lm[e[-2]*9 + m[-2]*3 + e[-1]] += 1
        
    lmc=[0]*27
    sc=0

    st=e[-1]*9 + m[-1]*3
    
    for i in range(st,st+3):
        lmc[i]=int(lm[i])
        sc+=lmc[i]
        
    ra=random.randrange(sc)

    for i in range(27):
        ra-=lmc[i]
        if ra<0:
            break

    s=(i+1)%3

else:
    s=1
    
m+=[s]

if s==0:
    output = "P" # paper beats rock    
elif s==1:
    output = "S" # scissors beats paper
else:
    output = "R" # rock beats scissors