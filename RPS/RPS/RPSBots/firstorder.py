from random import choice

class Model:
	def __init__(self):
		self.r = 0
		self.p = 0
		self.s = 0

	def agregar(self, jugada):
		if jugada == "R":
			self.r+=1
		elif jugada == "P":
			self.p+=1
		else: 
			self.s+=1

	def jugar(self):
		m = max(self.r, self.p, self.s)
		if m == self.r:
			return "P"
		elif m == self.p:
			return "S"
		return "R"


if input == "":						# First round
	models = {"R" : Model(), "P" : Model(), "S" : Model()}
	output = choice(["R", "P", "S"])

elif anterior == "":				# Second round
	output = choice(["R", "P", "S"])	

else:								# Other rounds
	models[anterior].agregar(input)
	output = models[input].jugar()

anterior = input