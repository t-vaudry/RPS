import random

if input == '':
    memory = ''
    rotate0 = 0.0
    rotate1 = 0.0
    rotate2 = 0.0
    currentrotation = 0
else:
    if input == 'R':
        if previousout == 'R':
            rotate1 += 1
            rotate2 -= 1
            memory += '1'
        elif previousout == 'P':
            rotate0 += 1
            rotate1 -= 1
            memory += '2'
        else:
            rotate2 += 1
            rotate0 -= 1
            memory += '3'
    elif input == 'P':
        if previousout == 'R':
            rotate2 += 1
            rotate0 -= 1
            memory += '4'
        elif previousout == 'P':
            rotate1 += 1
            rotate2 -= 1
            memory += '5'
        else:
            rotate0 += 1
            rotate1 -= 1
            memory += '6'
    else:
        if previousout == 'R':
            rotate0 += 1
            rotate1 -= 1
            memory += '7'
        elif previousout == 'P':
            rotate2 += 1
            rotate0 -= 1
            memory += '8'
        else:
            rotate1 += 1
            rotate2 -= 1
            memory += '9'

rotate0 *= 0.9
rotate1 *= 0.9
rotate2 *= 0.9
 
if rotate2 > rotate0 and rotate2 > rotate1:
    currentrotation += 2
    currentrotation %= 3
    temp = rotate0
    rotate0 = rotate2
    rotate2 = rotate1
    rotate1 = temp
elif rotate1 > rotate0 and rotate1 > rotate2:
    currentrotation += 1
    currentrotation %= 3
    temp = rotate0
    rotate0 = rotate1
    rotate1 = rotate2
    rotate2 = temp
    
   

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
    if currentrotation == 0:
        if prediction == '1' or prediction == '2' or prediction == '3':
            output = 'P'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            output = 'S'
        else:
            output = 'R'
    elif currentrotation == 1:
        if prediction == '1' or prediction == '2' or prediction == '3':
            output = 'S'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            output = 'R'
        else:
            output = 'P'
    else:
        if prediction == '1' or prediction == '2' or prediction == '3':
            output = 'R'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            output = 'P'
        else:
            output = 'S'

        
        
previousout = output