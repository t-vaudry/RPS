import random
from math import exp,sqrt

gamma = 0.9
alpha = 0.01
def isNaN(num):
    return num != num
def weighted_choice(choices):
        #print(choices)
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
        init = exp(alpha*gamma/3.0*sqrt(1000.0/3.0))
        w = [init,init,init]
        output = random.choice(["R", "P", "S"])
        choices = [("R",1.0/3.0),("P",1.0/3.0),("S",1.0/3.0)]
        seq_out.append(output)
        s = 3.0
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
                c,p = choices[i]
                x = 0
                if alt[i]==seq_out[-1]:
                        x = rew[seq_out[-1]]/p
                w[i]=w[i]*exp(gamma/9.0*(x+alpha/(p*3.0*1000)))
                                      

        s = 0
        for i in range(0,3):
                s += w[i]

        for i in range(0,3):
                p = (1.0 - gamma)*w[i]/s + gamma/3.0
                if(isNaN(p)):
                        p = 1.0/3.0
                choices[i] = (alt[i], p)

        output = weighted_choice(choices)
        seq_out.append(output)