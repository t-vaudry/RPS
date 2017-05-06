import random, collections

TACTICS = ["R", "P", "S"]
BACK_MEMORY = 2

def winner(opponent_tactic):
    return TACTICS[(TACTICS.index(opponent_tactic) + 1) % 3]

def most_common_element(l):
    return max(set(l), key=l.count)

hist = ""

if input == "":
    output = random.choice(TACTICS)
else:
    hist = hist + input
    if len(hist) < 4:
        output = winner(random.choice([s for s in hist]))
    else:
        actions = collections.defaultdict(list)
        for i in range(len(hist)-(BACK_MEMORY)):
            actions[hist[i:i+BACK_MEMORY]].append(hist[i+BACK_MEMORY])
        last_opponent_actions = hist[-BACK_MEMORY:]
        if last_opponent_actions in actions:
            output = winner(most_common_element(actions))
        else:
            output = winner(random.choice([s for s in hist]))