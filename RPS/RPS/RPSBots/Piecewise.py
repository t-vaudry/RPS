import random

if not input:
  turns = 0
else:
  turns += 1

if turns < 300:
  output = random.choice(('R', 'P', 'S', 'S'))
elif turns < 525:
  output = random.choice(('R', 'P', 'S', 'P'))
elif turns < 693:
  output = random.choice(('R', 'P', 'S', 'R'))
elif turns < 819:
  output = random.choice(('R', 'P', 'S', 'S'))
elif turns < 913:
  output = random.choice(('R', 'P', 'S', 'P'))
elif turns < 983:
  output = random.choice(('R', 'P', 'S', 'R'))
else:
  output = random.choice(('R', 'P', 'S', 'S'))