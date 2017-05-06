from collections import defaultdict

def beats(x):
    if x == 'rock':
        return 'paper'
    elif x == 'paper':
        return 'scissors'
    elif x == 'scissors':
        return 'rock'

def tr(x):
    return {'R': 'rock', 'P': 'paper', 'S': 'scissors'}[x]

def untr(x):
    return {'rock': 'R', 'paper': 'P', 'scissors': 'S'}[x]

if input == "":
    input2 = []
    output = "R"
else:
    n = 7
    freqs = defaultdict(int)
    input2.append(tr(input))

    if len(input2) < n:
        output = "R"
    else:
        freqs[tuple(input2[~(n-1):])] += 1
        movestats = [(freqs[tuple(moves)], moves[-1]) for moves in [input2[~(n-2):] + [move] for move in ['rock', 'paper', 'scissors']]]
        r = beats(max(movestats)[1])
        output = untr(r)