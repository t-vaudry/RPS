import random

if input == "":
     beater = 'R'
     same = 'P'
     var = 1
     output = random.choice(['P','R','S'])
elif var == 1:
     output = same
     if input == 'R':
          same = 'R'
          beater = 'P'
     if input == 'P':
          same = 'P'
          beater = 'S'
     if input == 'S':
          same = 'S'
          beater = 'R'
     var = 0
else:
      var = 1
      output = beater