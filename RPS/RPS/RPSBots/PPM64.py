# This entry is based on Prediction by Partial Matching, a method that is used
# in data compression.

import random
from collections import defaultdict

CONTEXT_SIZE=64

if input == "":
    contexts = defaultdict(lambda: [0.1, 0.1, 0.1])
    history  = ''
else:
    input_idx = ['R', 'P', 'S'].index(input)

    # Update empty context
    contexts[''][input_idx] += 1

    # Update other contexts
    for i in range(1, min(CONTEXT_SIZE, len(history)+1)):
        contexts[history[-i:]][input_idx] += 1

    history += input
    history += output

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

# Predict the opponent move from the context, then beat it. This is
# randomized to avoid being predictable.
choice = random.random() * sum(best_context)
if choice < best_context[0]:
    output = 'P' # Paper beats Rock
elif choice < best_context[0] + best_context[1]:
    output = 'S' # Scissors beat Paper
else:
    output = 'R' # Rock beats Scissors