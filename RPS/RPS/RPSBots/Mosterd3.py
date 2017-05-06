if input == "":
    import re
    opponentMoves = ""
else:
    opponentMoves += input

opponentMoves = opponentMoves[25:]


likely = {'R': 0, 'P': 0, 'S': 0}
for i in range(1, len(opponentMoves) - 1):
    pattern = opponentMoves[-i:] + "."
    for match in re.findall(pattern, opponentMoves):
        likely[match[-1]] += 1

opponent_prediction = max(likely, key=lambda m: likely[m])

if opponent_prediction == 'R':
    output = 'P'
elif opponent_prediction == 'P':
    output = 'S'
elif opponent_prediction == 'S':
    output = 'R'