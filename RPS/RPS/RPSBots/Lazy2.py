if input == "":
	choices = [('R', 0), ('P', 0), ('S', 0)]

choices = sorted(choices, key=lambda choice: choice[1])

choices[0] = (choices[0][0], choices[0][1] + 1)

output = choices[0][0];