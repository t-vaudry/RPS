import random

defeats = {
    'R': 'S',
    'S': 'P',
    'P': 'R',
}


def won_last(us, opponent):
    return defeats[us] == opponent



output = ''

won = False
opponent_last = input

if input == '':
    # First move
    last = ''
    opponent_last = ''
else:
    print last, opponent_last
    won = won_last(last, opponent_last)

if input == 'R':
    if won:
        output = 'R'
elif input == 'P':
    if won:
        output = 'P'
elif input == 'S':
    if won:
        output = 'S'
if not output:
    output = random.choice(['R', 'P', 'S'])

last = output