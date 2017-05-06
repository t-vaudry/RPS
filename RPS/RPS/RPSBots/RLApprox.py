import random
import math

nwin = 0
ntie = 0
nloss = 0
iter = 0
epsilon = 0.2
#input = ""
#while True:
preLen = 4

if not input:
    O = [random.choice('RPS') for i in range(preLen)]
    A = [random.choice('RPS') for i in range(preLen)]
    score = {
        ('R', 'R'): -1, ('R', 'P'): -2, ('R', 'S'): 1,
        ('P', 'R'): 1, ('P', 'P'): -1, ('P', 'S'): -2,
        ('S', 'R'): -2, ('S', 'P'): 1, ('S', 'S'): -1
    }
#   score = {
#       ('R', 'R'): 0, ('R', 'P'): -1, ('R', 'S'): 1,
#       ('P', 'R'): 1, ('P', 'P'): 0, ('P', 'S'): -1,
#       ('S', 'R'): -1, ('S', 'P'): 1, ('S', 'S'): 0
#   }
    num = {'R': 1, 'P': 2, 'S': 3, 1: 1}
    lr = 1
    lam = 0.01
    weights = {'R': [0] * (2*preLen + 1), 'P': [0] * (2*preLen + 1), 'S': [0] * (2*preLen + 1)}  # add the constant term
    Gweights = weights.copy()

    def Q(state, action):
        return sum(weights[action][x] * num[state[x]] for x in range(len(state)))


    output = random.choice('RPS')
else:
    input = input.upper()
    state = tuple(O[-preLen:] + A[-preLen:] + [1])
    # state = tuple(O[-preLen:] + [1])
    action = output
#    print "program gives: %s" % output
    if score[(output, input)] == 1:
        nloss += 1
    elif score[(output, input)] == -1:
        ntie += 1
    elif score[(output, input)] == -2:
        nwin += 1

    reward = score[(action, input)]
    O.append(input)
    A.append(output)
    newstate = tuple(O[-preLen:] + A[-preLen:] + [1])
    # newstate = tuple(O[-preLen:] + [1])
    maxvalue = max(Q(newstate, a) for a in 'RPS')

    dweights = [(reward + 0.9 * maxvalue - Q(state, action)) * num[state[x]] for x in range(len(state))]
    Gweights[action] = [Gweights[action][x] + dweights[x] ** 2 for x in range(len(state))]
    weights[action] = [weights[action][x] + lr/float(math.sqrt(Gweights[action][x] + lam)) * dweights[x] for x in range(len(state))]
    succ = [Q(newstate, a) for a in 'RPS']
    optimal_actions = ['RPS'[x] for x in range(len(succ)) if succ[x] == max(succ)]
    output = random.choice(optimal_actions) if random.random() > epsilon else random.choice('RPS')