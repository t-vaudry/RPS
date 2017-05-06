# This entry is based on Prediction by Partial Matching, a method that is used
# in data compression.

from collections import defaultdict

CONTEXT_SIZE=16

if input == "":
    score     = { 'RR':  0, 'RP': -1, 'RS':  1,
                  'PR':  1, 'PP':  0, 'PS': -1,
                  'SR': -1, 'SP':  1, 'SS':  0 }
    contexts1 = defaultdict(lambda: [0.1, 0.1, 0.1])
    contexts2 = defaultdict(lambda: [0.1, 0.1, 0.1])
    history1  = ''
    history2  = ''
    scounts   = [1.0]*6
    schoice   = None

    def update_contexts(input, output, contexts, history):
        input_idx = 'RPS'.index(input)

        # Update empty context
        contexts[''][input_idx] += 1

        # Update other contexts
        for i in range(1, min(CONTEXT_SIZE, len(history)+1)):
            contexts[history[-i:]][input_idx] += 1

        history += input
        history += output

        return history

    def predict(contexts, history):
        # Find the best context to use for prediction. The best context has the highest
        # "Most-probable Symbol"-Probability.
        best_context = contexts['']
        best_mpsp    = max(contexts['']) / (1 + sum(contexts['']))

        for i in range(1, min(CONTEXT_SIZE, len(history)+1)):
            c = contexts[history[-i:]]
            mpsp = max(c) / (1 + sum(c))
            if mpsp > best_mpsp:
                best_context = c
                best_mpsp = mpsp
            elif mpsp == best_mpsp:
                # Merge equally good contexts
                best_context[0] += c[0]
                best_context[1] += c[1]
                best_context[2] += c[2]

        return best_context.index(max(best_context))

else:
    history1 = update_contexts(input, output, contexts1, history1)
    history2 = update_contexts(output, input, contexts2, history2)

    scounts = map(lambda x: x * 0.9, scounts)

    for i, c in enumerate(choices):
        scounts[i] += score[c + history2[-1]]

# Sicilian Reasoning
p0 = predict(contexts1, history1)
p1 = (1 + p0) % 3
p2 = (2 + p0) % 3
m0 = predict(contexts2, history2)
m1 = (1 + m0) % 3
m2 = (2 + m0) % 3

choices = [p0, p1, p2, m0, m1, m2]
choices = map(lambda x: 'PRS'[x], choices)
schoice = scounts.index(max(scounts))

output = choices[schoice]