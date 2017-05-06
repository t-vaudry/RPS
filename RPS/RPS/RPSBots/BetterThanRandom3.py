from random import choice as p
m={"R":"P","P":"S","S":"R"}
r,b=[],m.keys()
s=[0]*len(b)
while len(r)<101:
    r+=p(b)
for c in r:
    s[b.index(c)]+=1
output=m[b[s.index(max(s))]]