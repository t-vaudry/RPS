if input == "":
    count = 0

if count % 3 == 0:
    output = "R"
    count = 1
elif count % 3 == 1:
    output = "P"
    count = 2
elif count % 3 == 2:
    output = "S"
    count = 0