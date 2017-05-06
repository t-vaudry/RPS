if input == "":
    state = id(0)

state = id(state)

output = ("R", "P", "S")[state % 3]