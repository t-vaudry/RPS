import random

def get_most_likely(ij) :
   r = results[ij]['R']
   p = results[ij]['P']
   s = results[ij]['S']
   total = r+p+s
   prob_moves = {"P":r/total,"S":p/total,"R":s/total}
   random_num = random.uniform(0,1)
   for move, prob in prob_moves.items():
       if random_num < prob :
           break
       random_num = random_num - prob
   return move 

moves = ['R','P','S']

if input not in moves:
    results = {}
    count = 1
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
    count += 1 
    if count > 800 :
        output = get_most_likely(ij)
    else :
        output = random.choice(moves)
    last_input = input
    last_output = output