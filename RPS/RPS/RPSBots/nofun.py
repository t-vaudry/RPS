import random

WIN = {"R":"P","P":"S","S":"R"}

if not input:
  buf = ["R","S","P"]
  output = "P"
else:
  buf.append(input)
  output = random.choice(buf)
  output = WIN[output]