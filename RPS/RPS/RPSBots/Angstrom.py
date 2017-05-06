import random

if input == "":
    index = {"R": 0, "P": 1, "S": 2}
    counts = [0, 0, 0]
    name = ("R", "P", "S")
    output = random.choice(name)
else:
    counts[index[input]] += 1
    for i in xrange(3):
        counts[i] *= 0.98
    sample = [random.gammavariate(n + 1, 1) for n in counts]
    expected_values = [sample[2] - sample[1],
                       sample[0] - sample[2],
                       sample[1] - sample[0]]
    output = name[expected_values.index(max(expected_values))]