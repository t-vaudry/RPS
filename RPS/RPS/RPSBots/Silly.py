import random

plays = ["R","P","S"]
counter = {"R":"P", "P":"S", "S":"R"}

if input == "":
    round = 0
    hist = []
    output = "R"
else:
    if round<100:
      hist.append(input)
    else:
      hist[round % 10] = input
    guess = random.choice(hist)
    output = counter[guess]
    round += 1