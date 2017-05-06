import random

class Prob():
	def __init__(self):
		self.R = 1.0
		self.P = 1.0
		self.S = 1.0
	
	def update(self, type):
		if (type == "R"):
			self.R += 1.0

		elif (type == "P"):
			self.P += 1.0

		elif (type == "S"):
			self.S += 1.0
		total = (self.R + self.P + self.S) / 3.0
		self.R /= total
		self.P /= total
		self.S /= total
		
	def getProbs(self):
		return {"R":self.R, "P":self.P, "S":self.S}

	def getLikely(self):
		P = self.getProbs()
		C = random.choice([(k,v) for k,v in P.items() if v == P[max(P,key=P.get)]])
		return C[0]

	def getOpposite(self, type):
		if (type == "R"):
			return "P"
		elif (type == "P"):
			return "S"
		else:
			return "R"


if input == "":
	B = Prob()
else:
	B.update(input)

output = B.getOpposite(B.getLikely())