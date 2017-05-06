import random

if input == '':
    memory = ''
else:
    if input == 'R':
        if previousout == 'R':
            memory += '1'
        elif previousout == 'P':
            memory += '2'
        else:
            memory += '3'
    elif input == 'P':
        if previousout == 'R':
            memory += '4'
        elif previousout == 'P':
            memory += '5'
        else:
            memory += '6'
    else:
        if previousout == 'R':
            memory += '7'
        elif previousout == 'P':
            memory += '8'
        else:
            memory += '9'
    

loc = -1
for i in range(1,len(memory)-1):
    thisloc = memory[:-1].rfind(memory[-i:])
    if thisloc != -1:
        loc = thisloc+i
    else:
        break


if loc == -1:
    output = random.choice(['R','P','S'])
else:
    prediction = memory[loc]
    if prediction == '1' or prediction == '2' or prediction == '3':
        output = 'P'
    elif prediction == '4' or prediction == '5' or prediction == '6':
        output = 'S'
    else:
        output = 'R'
        
previousout = output