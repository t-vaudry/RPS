import random

if random.randint(0, 2):
    if not input == "":
        output = input
    else:
        output = random.choice("RPS")
else:
    output = random.choice("RPS")