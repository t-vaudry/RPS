def z():
	return {'R':0,'P':0,'S':0}

if not input:
	import random
	from collections import defaultdict
	m={}
	for i in range(2,15):
		m[i]=defaultdict(z)
	h=""
	random.seed()

w = {'R':1,'P':1,'S':1}

for i,c in m.iteritems():
	if len(h)< i:
		continue
	c[h[-i:]][input]+=i

h+=input

for i,c in m.iteritems():
	if len(h)< i:
		continue
	for k,v in c[h[-i:]].iteritems():
		w[k]+=v

d = random.uniform(0,sum(w.values()))
for k,v in w.iteritems():
	d-=v
	if d<=0:
		output = {'R':'P','P':'S','S':'R'}[k]
		break