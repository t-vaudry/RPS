import random
if not input :
    moves = ["R", "P", "S"]
    did_lose = {"R":"P", "P":"S", "S":"R"}
    current_choice = random.choice(moves)
    num_times = 1
    output = current_choice
else :
    if did_lose[current_choice] == input :
        last_choice = current_choice
        while current_choice == last_choice :
            current_choice = random.choice(moves)
        num_times = 0
    num_times += 1
    output = current_choice