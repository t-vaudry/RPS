import random

tactics = ["R", "P", "S"]

def winner(opponent_tactic):
    return tactics[(tactics.index(opponent_tactic) + 1) % 3]

hist = ""

if input == "":
    output = random.choice(tactics)

else:
    hist = hist + input
    output = winner(hist[-1])