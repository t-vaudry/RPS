run = ""

if input == "":
    output = "P"
else:
    if not input == "":
        run = input

    if input == run:
        if run == "R":
            output = "S"
        elif run == "S":
            output = "P"
        elif run == "P":
            output = "R"
    else:
        output = "P"