import random


if input == "":
    report = []
    output = "R"
else:
    def check_result(output, input):
        if (output == "S" and input == "P") or \
           (output == "P" and input == "R") or \
           (output == "R" and input == "S"):
            return 1
        if (output == "S" and input == "R") or \
           (output == "P" and input == "S") or \
           (output == "R" and input == "P"):
            return -1
        else:
            return 0
    result = check_result(output, input)
    report.append([output, input, result])
    last_turn = report[-1]
    if (last_turn[2] == 0):
        output = last_turn[0]
    elif (last_turn[2] == 1):
        output = last_turn[1]
    else:
        output = random.choice(["R","P","S"])