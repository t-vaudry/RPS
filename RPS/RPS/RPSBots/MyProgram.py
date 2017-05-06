if input == "":
    previous = "S"
    output = "S"
if input == "S":
    output = "R"
if input == "R":
    output = "P"
if input == "P":
    output = "S"
if input == "S" and previous == "S":
    output = "S"
if input == "R" and previous == "R":
    output = "R"
if input == "P" and previous == "P":
    output = "P"