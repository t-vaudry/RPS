import random

alpha = 0.1

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
        scores = [0,0,0]
        output = random.choice(["R", "P", "S"])
else:
        seq_in.append(input)
        rew = [0,0,0]
        if input == "R":
                rew[0] = 0.5
                rew[1] = 1
                rew[2] = 0
        if input == "P":
                rew[0] = 0
                rew[1] = 0.5
                rew[2] = 1
        if input == "S":
                rew[0] = 1
                rew[1] = 0
                rew[2] = 0.5

        for i in range(0,3):
            scores[i]+=rew[i]

        s = 0
        for i in range(0,3):
                s+=(1+alpha) ** scores[i]

        choices = [("R",0),("R",0),("R",0)]
        alt = ["R", "P", "S"]
        for i in range(0,3):
                choices[i] = (alt[i], ((1+alpha) ** scores[i]) / s)

        output = weighted_choice(choices)
        seq_out.append(output)