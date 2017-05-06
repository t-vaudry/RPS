import random

if input == '':
  output = 'P'
else:
  if not ((output == 'P' and input == 'R') or (output == 'S' and input == 'P') or (output == 'R' and input == 'S')):
    if (output == 'R'):
      output = random.choice(('P', 'S'))
    elif (output == 'P'):
      output = random.choice(('R', 'S'))
    else:
      output = random.choice(('R', 'P'))