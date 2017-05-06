if input == "":
    last = ["R"] * 9
    prev = "R"
    ctx = 0
else:
    last[ctx] = input
    ctx = ((ctx * 3) + {"R":0,"P":1,"S":2}[prev]) % 9
output = prev = {"R":"P","P":"S","S":"R"}[last[ctx]]