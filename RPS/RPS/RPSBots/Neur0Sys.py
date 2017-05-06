if not input:
    from random import random
    from math import exp
    from math import log
    def ln(x):return log(x) if x>=(3e-324) else -745
    conf=1
    weights=[[1.0/3.0,1.0/3.0,1.0/3.0]]
    links=[[0,0,0]]
    history=[]
    p=[1.0/3.0,1.0/3.0,1.0/3.0]
else:
    input={"R":0,"P":1,"S":2}[input]
    output={"R":0,"P":1,"S":2}[output]
    target=[[0.0,1.0,0.0],[0.0,0.0,1.0],[1.0,0.0,0.0]][input][output]
    conf+=(target-conf)*0.5
    target=[[0.0,1.0,0.0],[0.0,0.0,1.0],[1.0,0.0,0.0]][input]
    link=0
    pos=len(history)
    while True:
        weights[link]=[(weights[link][x]+target[x])*0.5 for x in xrange(0,3)]
        if not pos: break
        pos-=1
        link=links[link][history[pos]]
        if not link: break
    history+=[input]
    link=0
    pos=len(history)-1
    numer=denom=[1.0,1.0,1.0]
    depth=-40
    while True:
        numer=[numer[x]*2.0*weights[link][x] for x in xrange(0,3)]
        denom=[denom[x]*(1.0-weights[link][x]) for x in xrange(0,3)]
        depth+=1
        if not depth: break
        if not pos: break
        pos-=1
        nxtlink=links[link][history[pos]]
        if not nxtlink:
            links[link][history[pos]]=len(links)
            links+=[[0,0,0]]
            weights+=[[1.0/3.0,1.0/3.0,1.0/3.0]]
            break
        link=nxtlink
    p=[ln(numer[x])-ln(denom[x]) for x in xrange(0,3)]
    p=[0.0 if x<-709.0 else 1.0/(2.0*exp(-x)+1.0) for x in p]
    p=[conf*x+(1-conf)*(1.0/3.0) for x in p]
p=[float(x)/sum(p) for x in p] if sum(p) else [1.0/3.0,1.0/3.0,1.0/3.0]
choice=random()
output="R" if choice<p[0] else "P" if choice<1-p[2] else "S"