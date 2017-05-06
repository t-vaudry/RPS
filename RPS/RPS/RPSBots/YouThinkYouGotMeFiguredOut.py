if (input == ''):
    seed = 7
    offset = 0
    rounds = 0
    offsetCounter = 14
m = 7
k = 3

if (rounds % offsetCounter == 0):
    offset = offset + 1
    offsetCounter = (seed % 14) + 1

seed = ((seed + k) * m) % 31
output = ["R", "P", "S"][(seed + offset) % 3]
rounds = rounds + 1