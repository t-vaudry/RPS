import random, operator, re
import os.path 
file_name = "persist_smilelearner_data"


DEBUG_ENABLED = True


def debug_data(*args):
	if DEBUG_ENABLED:
		print args

# helper : file handler
def persist_data(game_data):
	# debug_data("writting:" , game_data)
	file = open(file_name, "w")
	file.write(str(game_data))
	file.close()

def read_data(): #just reading one line?
	file = open(file_name, 'r')
	early_data = file.read()
	# debug_data(early_data, "in file.")
	file.close()
	return eval(early_data)



# gd = {}
if not input:
	gd = {} #game_data
	gd["valid_outputs"]  = ["R", "P", "S"]
	gd["move_count"]  = {'R':0, 'P':0 ,'S':0}
	gd["winner"]  = {"R":"P" , "P":"S", "S":"R"}
	gd["past_moves"] = ""
	gd["move_played_indexes"] = {'R':[],'P':[],'S':[]}
	gd["count"]=0
	count = gd["move_count"]
# else:
	# gd = read_data()
else:
	gd["move_count"][input] += 1
	gd["past_moves"] += input
	gd["count"] += 1 
	gd["move_played_indexes"][input] = gd["count"]
	# persist_data(gd)

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
	if not input or len(gd["past_moves"]) < 4:
		return get_random_output(gd["valid_outputs"])
	else:
		all_moves = gd["past_moves"]
		last_pattern = all_moves[-3:]+"[RPS]"
		matched_pattern = re.findall(last_pattern, all_moves)
		next_char_possibility_set = [ patt[-1] for patt in matched_pattern ]
		# debug_data("patterns:", matched_pattern, next_char_possibility_set, "lst:",last_pattern)
		if len(next_char_possibility_set) > 1:
			return get_max_occured_element(next_char_possibility_set)
		else:
			return "R"

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


# debug_data(input,"-",output)