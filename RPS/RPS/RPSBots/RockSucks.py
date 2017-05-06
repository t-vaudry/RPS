# I'm curious how the bots do against this--there is a simple strategy
# that soundly defeats it.  It should do _substantially_ worse than
# random.
import random

if input == "":
    choices = ["R", "P", "S"]

    # man, screw rock.  rock sucks!
    choices.remove("R")

output = random.choice(choices)