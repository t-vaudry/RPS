import random

if input == "":
    output = "R"
else:
    output = {'R':'P','P':'S','S':'R'}[input]
    
random.seed(0)