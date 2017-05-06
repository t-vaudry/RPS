import random

epsilon=0.1
a = 1000.0
def weighted_choice(choices):
        total = sum(w for c, w in choices)
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices:
                if upto + w > r:
                        return c
                upto += w
        assert False, "Shouldn't get here"


choices = [("R",a/(2*a-1.0)+epsilon),("P",0),("S",(a-1.0)/(2*a-1.0)-epsilon)]
output = weighted_choice(choices)