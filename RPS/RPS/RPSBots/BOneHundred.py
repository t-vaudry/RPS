import random
import collections

size = 3

try:
    prev
except NameError:
    prev = collections.deque([])

output = ""

if input == "":
    for i in range(size):
        prev.append(random.choice(["R", "P", "S"]))
    output = random.choice(["R", "P", "S"]);
else:
    prev.appendleft(input)
    prev.pop()
    guess = random.choice(prev)
    
    if guess == "R":
        output = "P"
    elif guess == "P":
        output = "S"
    elif guess == "S":
        output = "R"