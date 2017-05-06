import random
ans = ['R','P','S']
if input == '':
    usr = ['']
    com = []
    rnd = 0
    com.append(random.choice(ans))
else:
    usr.append(input)
if com[rnd] == 'R':
    if usr[rnd] == 'P':
        com.append(random.choice(ans))
    else:
        com.append(com[rnd])
elif com[rnd] == 'P':
    if usr[rnd] == 'S':
        com.append(random.choice(ans))
    else:
        com.append(com[rnd])
elif com[rnd] == 'S':
    if usr[rnd] == 'R':
        com.append(random.choice(ans))
    else:
        com.append(com[rnd])
output = com[rnd+1]
rnd += 1