if not input:
    from random import random
    p=w=[1.0/3.0]*3
    h=[]
    r=1
if input:
    h+=[{"R":0,"P":1,"S":2}[input]]
    output={"R":0,"P":1,"S":2}[output]
if len(h)>=2:
    r+=(([[0.0,1.0,0.0],[0.0,0.0,1.0],[1.0,0.0,0.0]][h[-1]][output])-r)*0.5
    for x in xrange(0,3): w[x]+=(([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]][(h[-1]-h[-2])%3])[x]-w[x])*0.5
    p=[r*w[(x+2-h[-1])%3]+(1-r)*(1.0/3.0) for x in xrange(0,3)]
p=[float(x)/sum(p) for x in p] if sum(p) else [1.0/3.0,1.0/3.0,1.0/3.0]
choice=random()
output="R" if choice<p[0] else "P" if choice<1-p[2] else "S"