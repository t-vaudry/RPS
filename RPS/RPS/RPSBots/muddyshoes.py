import random

if input == "":
    seq_length = 3
    seq_count = 0
    strats = ["random","rock","paper","scissors","RPS","PPS","SRR","RPR"]
    curr_strat = random.choice(strats)
else:
    seq_count += 1

if seq_count==seq_length:
    seq_count = 0
    seq_length = random.Random().randint(0,13)
    curr_strat = random.choice(strats)

if curr_strat == "random":
    output = random.choice(["R","P","S"])
elif curr_strat == "rock":
    output = "R"
elif curr_strat == "paper":
    output = "P"
elif curr_strat == "scissors":
    output = "S"
else:
    output = curr_strat[seq_count%3]