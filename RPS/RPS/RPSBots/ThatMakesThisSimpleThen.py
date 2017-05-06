import random
types = ['R','P','S']
if not input or not moves:
 next = random.randrange(3)
 moves = [types[next]] * random.randrange(1, 4)
 moves.append(types[next-1])

output = moves.pop(0)