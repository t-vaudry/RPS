if not input:
    import random
    rnd=random.random
    h=output=""
    s=[0]*486
    c={"R":0,"P":1,"S":2}

h+=output+input
p=[0]*3

if len(h)>9:
    h0=c[h[-1]]
    h1=c[h[-2]]
    h2=c[h[-3]]
    h3=c[h[-4]]
    h4=c[h[-5]]
    h5=c[h[-6]]
    h6=c[h[-7]]
    h7=c[h[-8]]
    h8=c[h[-9]]
    h9=c[h[-10]]
    s=[x*0.933 for x in s]
    n=0
    for x1 in xrange(3):
        for x2 in xrange(3):
            for x3 in xrange(3):
                for x4 in xrange(3):
                    t=(h9*x4+h7*x3+h5*x2+h3*x1-h0)%3
                    if t==0:
                        s[n+1]+=1
                        s[n+2]-=1
                    elif t==1:
                        s[n]+=1
                        s[n+1]-=1
                    else:
                        s[n]-=-1
                        s[n+2]+=1
                    t=(h7*x4+h5*x3+h3*x2+h1*x1)%3
                    if t==0:
                        p[0]+=s[n]
                        p[1]+=s[n+1]
                        p[2]+=s[n+2]
                    elif t==1:
                        p[0]+=s[n+2]
                        p[1]+=s[n]
                        p[2]+=s[n+1]
                    else:
                        p[0]+=s[n+1]
                        p[1]+=s[n+2]
                        p[2]+=s[n]
                    n+=3
                    if not(x1 or x3): continue
                    t=(h5*x4+h4*x3+h3*x2+h2*x1-h0)%3
                    if t==0:
                        s[n+1]+=1
                        s[n+2]-=1
                    elif t==1:
                        s[n]+=1
                        s[n+1]-=1
                    else:
                        s[n]-=-1
                        s[n+2]+=1
                    t=(h3*x4+h2*x3+h1*x2+h0*x1)%3
                    if t==0:
                        p[0]+=s[n]
                        p[1]+=s[n+1]
                        p[2]+=s[n+2]
                    elif t==1:
                        p[0]+=s[n+2]
                        p[1]+=s[n]
                        p[2]+=s[n+1]
                    else:
                        p[0]+=s[n+1]
                        p[1]+=s[n+2]
                        p[2]+=s[n]
                    n+=3

try:
    p=[2**(0.001*x) for x in p]
except:
    p=[1 if x==max(p) else 0 for x in p]
r=rnd()*sum(p)
output="R" if r<p[0] else "P" if r<p[0]+p[1] else "S"