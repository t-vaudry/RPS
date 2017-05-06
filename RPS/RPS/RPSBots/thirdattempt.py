import random

if input == "":
    rc, pc, sc = 1, 1, 1
elif input == "R":
    rc += 1
elif input == "P":
    pc += 1
elif input == "S":
    sc += 1

tc = rc + pc + sc

r = random.randint(1, tc)
if r <= rc:
    output = "P"
elif r <= rc + pc:
    output = "S"
else:
    output = "R"

change = { "RR": 0, "RP": -1, "RS": 1, "PR": 1, "PP": 0, "PS": -1, "SR": -1, "SP": 1, "SS": 0 }

if input == "":
   delta = 0
else:
   delta += change[last + input]

if delta > 10:
   output = random.choice(["R", "P", "S"])

last = output