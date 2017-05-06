import random

random.seed()
if input == "": 
	rockc = paperc = scissorsc = total = 0
        paper_range = rockc + paperc
elif input == "R":
	rockc += 1
        total  += 1
        paper_range += 1
elif input == "P":
	paperc += 1
        total    += 1
        paper_range += 1
elif input == "S":
	scissorsc += 1
        total += 1
if input != "":
        random_number = random.randrange(total)
        if random_number < rockc:
                output = "P"
        elif random_number < paper_range:
                output = "S"
        else:
                output = "R"
else:
        random_number = random.randrange(3)
        if random_number == 0:
                output = "P"
        elif random_number == 1:
                output = "S"
        else:
                output = "R"