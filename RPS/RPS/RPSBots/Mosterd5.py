if input == "":
    opponentMoves = ""
    opponentPredictions = {}
else:
    opponentMoves += input
    opponentMoves = opponentMoves[-25:]
    
    for i in range(1, len(opponentMoves)):
        pattern = opponentMoves[-i:]
        counter = opponentPredictions.get(pattern, 0)
        opponentPredictions[pattern] = counter + 1

likely = {'R': 0, 'P': 0, 'S': 0}
for move in "RPS":
    movePattern = opponentMoves + move

    for i in range(1, len(opponentMoves)):
        pattern = movePattern[-i:]

        counter = opponentPredictions.get(pattern, 0)
        likely[move] += counter

        if counter == 0:
            break
    
opponent_prediction = max(likely, key=lambda m: likely[m])

if opponent_prediction == 'R':
    output = 'P'
elif opponent_prediction == 'P':
    output = 'S'
elif opponent_prediction == 'S':
    output = 'R'