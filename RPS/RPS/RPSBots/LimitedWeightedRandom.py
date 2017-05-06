import random

if input == "":
    selection_list = ["R"]*10 + ["P"] * 10 + ["S"] * 10 #list limited to 30 elements
    random.shuffle(selection_list)
elif input == "R":
        selection_list.pop(0)
	selection_list += ["P"]
elif input == "P":
        selection_list.pop(0)
	selection_list += ["S"]
elif input == "S":
        selection_list.pop(0)
	selection_list += ["R"]

output  = random.choice(selection_list)