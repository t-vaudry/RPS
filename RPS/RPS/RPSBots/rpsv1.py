import random, operator

valid_outputs = ["R", "P", "S"]
move_count = {'R':0, 'P':0 ,'S':0}
winner = {"R":"P" , "P":"S", "S":"R"}

input="R"

move_count[input]+=1

def get_random_output():
	return  random.choice(valid_outputs)

def random_and_not_same_as_last():
	return random.choice(rem_elem(valid_outputs, input))

def process():
	if not input:
		return get_random_output()
	elif get_winner_tuple_of_most_used_elems(move_count)[1] < 20:
		return random_and_not_same_as_last()
	else:
		get_winner_tuple_of_most_used_elems(move_count)[0]

def rem_elem(old_arr, element):
	new_array  = old_arr[:]
	new_array.remove(element)
	return new_array

def get_winner_tuple_of_most_used_elems(dicts):
	return max(dicts.iteritems(), key= operator.itemgetter(1))


output = process()