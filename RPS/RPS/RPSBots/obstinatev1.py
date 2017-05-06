import random

if not input :
    moves = ["R", "P", "S"]
    did_lose = {"R":"P", "P":"S", "S":"R"}
    current_choice = random.choice(moves)
    num_times = 1
    output = current_choice
else :
    if did_lose[input] == current_choice :
        current_choice = random.choice(moves)
        num_times = 0
    num_times += 1
    output = current_choice