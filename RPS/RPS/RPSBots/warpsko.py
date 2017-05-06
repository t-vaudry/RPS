# http://arstechnica.com/science/2014/05/win-at-rock-paper-scissors-by-knowing-thy-opponent/

import random

outputs = "RPS"

if input == "":
    to_output = random.choice(outputs)
elif outputs.index(input) == (outputs.index(to_output) + 1) % 3:
    to_output = outputs[(outputs.index(input) + 1) % 3]
elif outputs.index(input) == (outputs.index(to_output) + 2) % 3 or input == to_output:
    to_output = outputs[(outputs.index(to_output) + random.choice([1, 2])) % 3]
else:
    to_output = random.choice(outputs)

output = to_output