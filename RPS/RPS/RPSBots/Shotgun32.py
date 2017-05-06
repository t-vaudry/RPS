import random
combos = [("R","S"),("P","R"),("S","P")]
if input:
    for i in range(len(throws)):
        if (throws[i], input) in combos:
            scores[i] += 1
        elif (input, throws[i]) in combos:
            scores[i] -= .5
        elif input == throws[i]:
            scores[i] += .5
    throws[3] = random.choice(throws[0:3])
    for i in combos:
         if input == i[0]:
            throws[4] = i[1]
    best = 0
    for i in range(len(history)):
        if throws[i] == input:
            history[i] += 1
        if history[i] > history[best]:
            best = i
        elif history[i] == history[best]:
           best = random.choice([i, best])
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
        elif scores[i] == scores[best]:
            best = random.choice([i, best])
    output = throws[best]
else:
    history = [0,0,0]
    scores = [0,0]
    throws = ["R","P","S"]
    for i in scores:
        throws.append("S")
    scores.extend([0,0,0])
    throws[3] = random.choice(throws[0:3])
    output = "S"