import random

epsilon=0.1
a = 1000.0
pr = 0.5
m = 5

def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
                if upto + w > r:
                        return c
                upto += w
        assert False, "Shouldn't get here"

#choices = [("R",a/(2*a-1.0)+epsilon),("P",0),("S",(a-1.0)/(2*a-1.0)-epsilon)]
choices = [("R",pr),("P",0),("S",1.0 - pr)]

if input=="":		
	restants = 0
else:
	if restants==0:
		if last==input:
			choices = [("R",1.0/3.0),("P",1.0/3.0),("S",1.0/3.0)]
			restants = m
	else:
		restants -= 1
		choices = [("R",1.0/3.0),("P",1.0/3.0),("S",1.0/3.0)]


last = weighted_choice(choices)
output = last