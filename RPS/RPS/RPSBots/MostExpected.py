# Variant of LeastExpected with a similar intention to break those markov chains

import random
winner = {"R": "P", "P": "S", "S": "R"}

if not input:
    mypattern = {}
    mypattern["R"] = {"R": 0, "P": 0, "S": 0}
    mypattern["P"] = {"R": 0, "P": 0, "S": 0}
    mypattern["S"] = {"R": 0, "P": 0, "S": 0}
    last = random.choice("RPS")
    output = random.choice("RPS")
else:
    now = mypattern[last]
    output = winner[winner[max(now, key=lambda m: now[m])]]

mypattern[last][output] += 1
last = output