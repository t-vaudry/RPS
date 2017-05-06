import random
import math
#input = ""
#while True:
if not input:
    K = 5  # Number of Hidden states
    E = 3  # Number of Evidence states R, P, S
    seqLen = 4

    def normalize(weights):
        total = sum(weights)
        return [1.0 * weight / total for weight in weights]

    def toInt(s):
        if s == 'R':
            return 0
        elif s == 'P':
            return 1
        elif s == 'S':
            return 2

    global startProb, transProb, emitProb
    startProb = [random.random() for h in range(K)]
    transProb = [[random.random() for h2 in range(K)] for h1 in range(K)]
    emitProb = [[random.random() for e in range(E)] for h in range(K)]
    output = random.choice(['R', 'P', 'S'])
    myGameSeq = ""
    urGameSeq = ""

    def forwardBackward(observation, startProb, transProb, emitProb):
        n = len(observation)

        def weight(h1, h2, i):
            # weight on edge from (H_{i-1} = h1) to (H_i = h2)
            w = 1.0
            if i == 0:
                w *= startProb[h2]
            else:
                w *= transProb[h1][h2]
            w *= emitProb[h2][observation[i]]
            return w

        forward = [None] * n
        for i in range(n):
            forward[i] = [None] * K
            for s in range(K):
                if i == 0:
                    forward[i][s] = weight(None, s, 0)
                else:
                    forward[i][s] = sum(forward[i - 1][h1] * weight(h1, s, i) \
                                        for h1 in range(K))
        backward = [None] * n
        for i in range(n - 1, -1, -1):
            backward[i] = [None] * K
            for s in range(K):
                if i == n - 1:
                    backward[i][s] = 1.0
                else:
                    backward[i][s] = sum(weight(s, h2, i + 1) * backward[i + 1][h2] \
                                         for h2 in range(K))
        return forward, backward


    def HMMPredict(urgame):
        global startProb, transProb, emitProb
        observation = [toInt(s) for s in urgame]

        length = len(observation)
        forward, backward = forwardBackward(observation, startProb, transProb, emitProb)
        Z = sum(forward[length - 1][s] for s in range(K))
        prob = [sum(sum(forward[length - 1][h4] / Z * transProb[h4][h5] * emitProb[h5][x] for h5 in range(K)) for h4 in
                    range(K)) for x in range(E)]

        u = random.random()
        if u < prob[0]:
            return 0
        elif prob[0] <= u < prob[0] + prob[1]:
            return 1
        else:
            return 2


    def HMMLearn(urgame, lam = 1e-6):  # urgames is the training set we got
        global startProb, transProb, emitProb
        # use EM to build the model

        observation = [toInt(s) for s in urgame]
        length = len(observation)
        for t in range(1):
            # E - step
            forward, backward = forwardBackward(observation, startProb, transProb, emitProb)
            Z = sum(forward[length - 1][s] for s in range(K))
            mu = [[forward[i][s] * backward[i][s] / Z for s in range(K)] for i in range(length)]
            tran = [[
                        [forward[i][s1] * transProb[s1][s2] * emitProb[s2][observation[i + 1]] * backward[i + 1][s2] / Z
                         for s2
                         in range(K)] for s1 in range(K)] for i in range(length - 1)]
            # M-step
            startCounts = [lam + mu[0][s] for s in range(K)]
            emitCounts = [[lam for e in range(E)] for h in range(K)]
            transCounts = [[lam for h2 in range(K)] for h1 in range(K)]

            for i in range(length):
                # update emission probabilities
                for s in range(K):
                    emitCounts[s][observation[i]] += mu[i][s]
                if i < length - 1:
                    for s1 in range(K):
                        for s2 in range(K):
                            transCounts[s1][s2] += tran[i][s1][s2]

            startProb = normalize(startCounts)
            for h in range(K):
                emitProb[h] = normalize(emitCounts[h])
                transProb[h] = normalize(transCounts[h])

else:
    myGameSeq += output
    urGameSeq += input
    if input == 'S':
        pass
    if len(myGameSeq) <= seqLen - 1:
        output = random.choice(['R', 'P', 'S'])
    elif len(myGameSeq) == seqLen:
        output = 'PSR'[HMMPredict(urGameSeq[-seqLen:])]
    else:
        assert (len(myGameSeq) > seqLen)
        HMMLearn(urGameSeq[-(seqLen+1):])
        output = 'PSR'[HMMPredict(urGameSeq[-seqLen:])]
#   input = raw_input("---------->")
#   print "computer gives " + output
#   for x in startProb:
#       print x