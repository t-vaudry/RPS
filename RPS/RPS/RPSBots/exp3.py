import random
from math import exp

gamma = 0.9

def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
                if upto + w > r:
                        return c
                upto += w
        assert False, "Shouldn't get here"


if input == "":
        seq_in = []
        seq_out = []
        w = [1.0,1.0,1.0]
        output = random.choice(["R", "P", "S"])
        choices = [("R",1.0/3.0),("P",1.0/3.0),("S",1.0/3.0)]
        seq_out.append(output)
else:
        seq_in.append(input)
        rew = {}
        if input == "R":
                rew["R"] = 0.5
                rew["P"] = 1
                rew["S"] = 0
        if input == "P":
                rew["R"] = 0
                rew["P"] = 0.5
                rew["S"] = 1
        if input == "S":
                rew["R"] = 1
                rew["P"] = 0
                rew["S"] = 0.5

        alt = ["R", "P", "S"]

        for i in range(0,3):
                if alt[i]==seq_out[-1]:
                        c,p = choices[i]
                        w[i]=w[i]*exp(gamma*rew[seq_out[-1]]/(3.0*p))

        s = 0
        for i in range(0,3):
                s += w[i]

        for i in range(0,3):
                choices[i] = (alt[i], (1.0 - gamma)*w[i]/s + gamma/3.0)

        output = weighted_choice(choices)
        seq_out.append(output)