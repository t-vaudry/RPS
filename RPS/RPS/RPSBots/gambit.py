import random

gambits = [
    ["R", "R", "R"],  # The Avalanche
    ["P", "P", "P"],  # The Bureaucrat
    ["P", "S", "R"],  # The Crescendo
    ["R", "S", "P"],  # The Denoument
    ["R", "P", "P"],  # Fistful O' Dollars
    ["P", "S", "S"],  # Paper Dolls
    ["P", "S", "P"],  # Scissor Sandwich
    ["S", "S", "S"]   # The Toolbox    
]

if input == "":
    n = 0
else:
    n += 1
    
index = n % 3
if index == 0:
    current_gambit = random.randrange(0, len(gambits))
    
output = gambits[current_gambit][index]