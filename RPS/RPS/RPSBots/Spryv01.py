# Spry v0.1 by Tom Theisen
# Not sure if it even runs

import random

length = 4
if input == "":
   current = ""
   history = {}
   
if len(current) == length:
   history[current] = history.get(current, "") + input

current = (current + input)[-length:]

if current in history:
   prediction = random.choice(history[current])
   output = {"R": "P", "P": "S", "S": "R"}[prediction]
else:
   output = random.choice("RPS")