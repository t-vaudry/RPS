import random

# Guesses opponent's next move as a function of two variables -
# my last move & the opponent's last move.
# This version always goes for the most likely option, rather 
# than a weighted choice. 

def get_most_likely(ij) :
   r = results[ij]['R']
   p = results[ij]['P']
   s = results[ij]['S']
   total = r+p+s
   prob_moves = {"P":r/total,"S":p/total,"R":s/total}
   return max(prob_moves,key = lambda i : prob_moves.get(i))

moves = ['R','P','S']

if input not in moves:
    results = {}
    output = random.choice(moves)
    last_output = output
    last_input = ""
    for i in moves :
        for j in moves :
            results[(i,j)] = {"R":1.0,"P":1.0,"S":1.0}
else :
    if last_input in moves :
	    results[(last_output,last_input)][input] = results[(last_output,last_input)][input] + 1.0
    ij = (last_output,input)
    output = get_most_likely(ij)
    last_input = input
    last_output = output