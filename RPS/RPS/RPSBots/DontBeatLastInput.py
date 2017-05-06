import random;
moves=["R","P","S"];

if input=="":
	output=random.choice(moves);
else:
	new=[];
	for m in moves:
		if m!=input:
			new.append(m);
	output=random.choice(new);