import random

selection_list = ["R"] + ["P"] + ["S"]


if input == "": 
	output = "R"


if ((output == "R" and input == "P") or (output == "P" and input == "S") or (output == "S" and input == "R")):
   output = random.choice(selection_list)