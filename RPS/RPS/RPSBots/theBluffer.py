import random
ans = ['R','P','S']
if input == '':
    usr = ['']
    com = []
    rnd = 0
    com.append(random.choice(ans))
else:
    usr.append(input)
if rnd >= 1:
    if com[rnd-1] == 'R':
        if usr[rnd] == 'P':
            com.append(random.choice(ans))
        else:
            com.append(com[rnd-1])
    elif com[rnd-1] == 'P':
        if usr[rnd] == 'S':
            com.append(random.choice(ans))
        else:
            com.append(com[rnd-1])
    else:
        if usr[rnd] == 'R':
            com.append(random.choice(ans))
        else:
            com.append(com[rnd-1])
output = com[rnd]
rnd += 1