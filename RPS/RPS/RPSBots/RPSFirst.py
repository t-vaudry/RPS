import random
valid_outputs = ["R", "P", "S"]

input = ""

def get_random_output():
	return  random.choice(valid_outputs)

def random_and_not_same_as_last():
	return random.choice(rem_elem(valid_outputs, input))

def process():
	if input=="":
		return get_random_output()
	else:
		return random_and_not_same_as_last()

def rem_elem(old_arr, element):
	new_array  = old_arr[:]
	new_array.remove(element)
	return new_array

output = process()