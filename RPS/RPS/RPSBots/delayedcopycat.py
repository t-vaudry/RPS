import random
history = ["R", "P", "S"]
call_sign = ["R", "P", "S"]
if input == "": # initialize variables for the first round
	output = random.choice(call_sign)
else:
        history.append(input)
        output = history[0]
        history = history.pop(0)