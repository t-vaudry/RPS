import random
import math

# lizardbeak!
# version 1.1
# a genetic algorith approach to RPS (maybe it'll work? I didn't think this through very well)

def build_population():
	i = 0
	while i < pop_size:
		j = 0
		new_sol = ""
		while j < sol_size:
			new_sol = ""
			new_sol+= random.choice(['R','P','S'])
			j+=1
		population.append(new_sol)
		i+=1
		
	
def get_last_score():
	# at this point output == the lizardbeak throw from last round
	if round<100:
		last_output = ga_output
	else:
		last_output = output
	
	if input=="":
		return 0
	if input==output:
		return 0
	if input=="R":
		if output=="S":
			return -1
		else:
			return 1	
	if input=="P":
		if output=="R":
			return -1
		else:
			return 1
	if input=="S":
		if output=="P":
			return -1
		else:
			return 1
	
# start doing stuff!

if input=="":
	#first round setup
	pop_size = 5
	sol_size = 10
	#mut_rate = 0.1 # again hardcoded for now due to lazyness
	#xover_rate = 0.6

	generation_size = 50
	round = 0
	gen_turn_count = 0
	ga_output = ""
	
	population = []
	pop_scores = [0,0,0,0,0] # hardcoded because I'm lazy right now
	build_population()
	throw_string = "".join(population)
	
else:
	round+=1

if round%generation_size == 0:
	if round > 0:
		# sort by fitness
		scores_and_pop = zip(pop_scores,population)
		scores_and_pop.sort()
		s_pop_scores, s_population = zip(*scores_and_pop)
		
		#clear the population and score lists
		del population[:]
		del pop_scores[:]
		
		# (lazy) select
		population.append(s_population[0])
		
		# (lazy) crossover
		xover_len = sol_size/2
		# 1,2 xover
		new_sol = s_population[0][:xover_len] + s_population[1][xover_len:]
		population.append(new_sol)
		new_sol = s_population[1][:xover_len] + s_population[0][xover_len:]
		population.append(new_sol)
		
		# 3,4 xover
		new_sol = s_population[2][:xover_len] + s_population[3][xover_len:]
		population.append(new_sol)
		new_sol = s_population[3][:xover_len] + s_population[2][xover_len:]
		population.append(new_sol)
		
		# mutate
		for s in population:
			mut_pos = random.randint(0,len(s)-1)
			s_l = list(s)
			s_l[mut_pos] = random.choice(['R','P','S'])
			s = "".join(s_l)
		
		# clear the s_pop_scores and s_population lists
		s_population = []
		s_pop_scores = []
		
	throw_string = "".join(population)
	pop_scores = [0,0,0,0,0]
	

# record the result of the last match in the fitness score list		
score = get_last_score()
sol_index1 = round/sol_size
sol_index = sol_index1%len(throw_string)
pop_scores[sol_index]+=score

# select what to throw!
throw_index = round%len(throw_string)
ga_output = throw_string[throw_index]
if round < 100:
	output = random.choice(['R','P','S'])
else:
	output = ga_output