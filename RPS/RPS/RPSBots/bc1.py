import math

def move2int(letterMove):
	if (letterMove == 'R'):
		return 0
	elif (letterMove == 'P'):
		return 1	
	elif (letterMove == 'S'):
		return 2
		
def int2move(intMove):
	if (intMove == 0):
		return 'R'
	elif (intMove == 1):
		return 'P'	
	elif (intMove == 2):
		return 'S'
		
if input == "": 
        history =  'RRRRRRRRRR'
        
history += input
outputfloat = 4.6-move2int(history[1])
outputmod = math.floor(outputfloat) % 3
output = int2move(outputmod)
history = history[1:]