'''
Updates:
-Removed some randomness.
-Made better than random (hopefully).
-Removed hobo blood dependency.
'''
import random as c
p = [("R","P"),("P","S"),("S","R")]
r =  c.choice(["R","P","S"])
for x in p:
    if r == x[0]:
        output = x[1]