import random

if input == '':
       output = random.choice(['S','R','P'])
else:
       if input == 'R':
              output = 'P'
       if input == 'S':
              output = 'R'
       else:
              output = 'S'