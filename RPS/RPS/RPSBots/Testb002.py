import random

if input == "":
    count = {'R':0, 'P':0, 'S':0}
else:
    count[input] += 1

if count['R'] < count['S'] and count['R'] < count['P']:
    output = 'R'
elif count['S'] < count['R'] and count['S'] < count['P']:
    output = 'S'
else:
    output = "P"