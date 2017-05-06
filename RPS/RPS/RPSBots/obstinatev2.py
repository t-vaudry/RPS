import random
if not input :
    moves = ["R", "P", "S"]
    history = ["R", "P", "S"]
    did_win = {"R":"S", "P":"R", "S":"P"}
    to_win = {"R":"P", "P":"S", "S":"R"}
    current_choice = random.choice(moves)
    num_times = 1
    output = current_choice
else :
    history.append(input)
    if did_win[current_choice] != input :
        last_choice = current_choice
        while current_choice == last_choice :
            current_choice = to_win[random.choice(history)]
        num_times = 0
    num_times += 1
    output = current_choice