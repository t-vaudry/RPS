import random
import math
if input == "":
	wR = random.randint(1,3)
	wP = random.randint(1,3)
	wS = random.randint(1,3)
elif input == "R":
	wS += 1
elif input == "P":
	wR += 1
elif input == "S":
	wP += 1
while True:
	t = random.randint(1,3)
	x = random.uniform(0,500)
        if t == 1:
		if x < math.fabs(random.gauss(0,wR)):
			output = "R"
			break
	elif t == 2:
		if x < math.fabs(random.gauss(0,wP)):
			output = "P"
			break
	elif t == 3:
		if x < math.fabs(random.gauss(0,wS)):
			output = "S"
			break