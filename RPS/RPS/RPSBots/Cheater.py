import random

if input == "":
    output = "R"
else: 
    output = {'R':'S','P':'R','S':'P'}[input]
    
r = random.random()
random.seed(0)