if not input:
	import random
	from collections import defaultdict
	memory={}
	for i in range(2,12):
		memory[i]=defaultdict(lambda: {'R':0,'P':0,'S':0})
	history=""
	random.seed()

weights = {'R':1,'P':1,'S':1}

for index,counts in memory.iteritems():
	if len(history)<(index):
		continue
	counts[history[-index:]][input]+=1

history+=input

for index,counts in memory.iteritems():
	if len(history)<(index):
		continue
	for k,v in counts[history[-index:]].iteritems():
		weights[k]+=v

totw=sum(weights.values())

decision = random.uniform(0,totw)
for k,v in weights.iteritems():
	decision-=v
	if decision<=0:
		output = k*len(k)
		break
output = ['R','P','S'][({'R':0,'P':1,'S':2}[output]+1)%3]