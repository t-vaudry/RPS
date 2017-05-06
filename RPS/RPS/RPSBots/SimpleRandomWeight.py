import random


def weighted_random_choice(rock_weight, paper_weight, scissor_weight):
    return random.choice(["R"] * rock_weight + ["P"] * paper_weight + ["S"] * scissor_weight)

if input == "":
    # First test / Setup.
    rock_weight = 1
    paper_weight = 1
    scissor_weight = 1
else:
    if input == "R":
        rock_weight += 1
    if input == "P":
        paper_weight += 1
    if input == "S":
        scissor_weight += 1

output = weighted_random_choice(rock_weight, paper_weight, scissor_weight)