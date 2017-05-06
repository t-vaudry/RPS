import random

if not input:
    record = []
    n = 0
    counts = {"R": 0, "P": 0, "S": 0}
    beat = {"R": "P", "P": "S", "S": "R"}

    def nonrandom(cs):
        high = max(cs.items(), key=lambda i: i[1])[0]
        low = min(cs.items(), key=lambda i: i[1])[0]

        if counts[high] * 0.8 > counts[low]:
            return high

    output = random.choice(['R', 'P', 'S'])
else:
    n += 1
    counts[input] += 1
    record.append(input)

    if not n % 10:
        random.seed()

    guess = nonrandom(counts)
    if n < 100 or not guess:
        output = random.choice(['R', 'P', 'S'])
    else:
        output = beat[guess]