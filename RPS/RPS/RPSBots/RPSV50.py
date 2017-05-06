import random, operator, re

DEBUG_ENABLED = False

if not input:
	gd = {} #game_data
	gd["valid_outputs"]  = ["R", "P", "S"]
	gd["move_count"]  = {'R':0, 'P':0 ,'S':0}
	gd["winner"]  = {"R":"P" , "P":"S", "S":"R"}
	gd["past_moves"] = ""
	gd["move_played_indexes"] = {'R':[],'P':[],'S':[]}
	gd["count"]=0
	count = gd["move_count"]
else:
	gd["move_count"][input] += 1
	gd["past_moves"] += input
	gd["count"] += 1 
	gd["move_played_indexes"][input] = gd["count"]

def get_random_output(valid_outputs):
	return  random.choice(valid_outputs)

def random_and_not_same_as_last(valid_outputs):
	return random.choice(rem_elem(valid_outputs, input))

def process():
	if not input:
		return get_random_output(gd["valid_outputs"])
	elif get_winner_tuple_of_most_used_elems(gd["move_count"])[1] < 10:
		return random_and_not_same_as_last(gd["valid_outputs"])
	else:
		return get_winner_tuple_of_most_used_elems(gd["move_count"])[0]

def get_by_pattern_from_past():
	if not input or len(gd["past_moves"]) < 3:
		return get_random_output(gd["valid_outputs"])
	else:
		for count in range(3,0,-1):
			possibilities = get_possibility(count)
			#debug_data(get_possibility(1),"f",count,";;;")
			if len(possibilities) >= 1:
				return gd["winner"][get_max_occured_element(possibilities)]
			else:
				return get_random_output(gd["valid_outputs"])

def get_possibility(char_count):
	all_moves = gd["past_moves"]
	last_pattern = all_moves[-char_count:]+"[RPS]"
	matched_pattern = re.findall(last_pattern, all_moves)
	next_char_possibility_set = [ patt[-1] for patt in matched_pattern ]
	return next_char_possibility_set
	# debug_data("patterns:", matched_pattern, next_char_possibility_set, "lst:",last_pattern)
	

def rem_elem(old_arr, element):
	new_array  = list(old_arr)
	new_array.remove(element)
	return new_array

def get_winner_tuple_of_most_used_elems(dicts):
	return max(dicts.iteritems(), key= operator.itemgetter(1))

def get_max_occured_element(elements):
	count = {'R':0, 'P':0 ,'S':0}
	for e in elements:
		count[e]+=1 	
	return get_winner_tuple_of_most_used_elems(count)[0]
	# return max(set(elements), elements.count)


output = get_by_pattern_from_past()