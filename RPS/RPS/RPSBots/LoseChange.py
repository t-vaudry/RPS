import random

if input == '':
  output = 'P'
else:
  if (output == 'R' and input == 'P') or (output == 'P' and input == 'S') or (output == 'S' and input == 'R'):
    if (output == 'R'):
      output = random.choice(('P', 'S'))
    elif (output == 'P'):
      output = random.choice(('R', 'S'))
    else:
      output = random.choice(('R', 'P'))