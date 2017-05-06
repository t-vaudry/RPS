import random

epsilon=0.1
def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
                if upto + w > r:
                        return c
                upto += w
        assert False, "Shouldn't get here"


choices = [("R",1-epsilon),("S",0),("P",epsilon)]
output = weighted_choice(choices)