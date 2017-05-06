if input=="":
    history = []
    c = {"R":0, "P":0, "S":0}
    output = "R"
else:
    history.append(input)
    c[input] += 1
    if c["R"] > c["P"] and c["R"] > c["S"]:
        output = "P"
    if c["S"] > c["R"] and c["S"] > c["P"]:
        output = "R"
    if c["P"] > c["S"] and c["P"] > c["R"]:
        output = "S"