import random

if input == "":
    rc, pc, sc = 0, 0, 0
elif input == "R":
    rc += 1
elif input == "P":
    pc += 1
elif input == "S":
    sc += 1

tc = rc + pc + sc

if tc < 100:
    output = random.choice(["R", "P", "S"])
else:
    r = random.randint(1, tc)
    if r <= rc:
        output = "P"
    elif r <= rc + pc:
        output = "S"
    else:
        output = "R"