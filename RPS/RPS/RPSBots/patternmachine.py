# author: blue-tomato
# 
# slight improvement on intelligent-string-finder-2

import random

randomthresh = 3.0
if input == '':
    memory = ''
    rotate0 = 0.0
    rotate1 = 0.0
    rotate2 = 0.0
    currentrotation = 0
    rotate0prime = 0.0
    rotate1prime = 0.0
    rotate2prime = 0.0
    currentrotationprime = 0
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
            
            
    if input == 'R':
        if simulateoutput == 'R':
            rotate1 += 1
            rotate2 -= 1
        elif simulateoutput == 'P':
            rotate0 += 1
            rotate1 -= 1
        elif simulateoutput == 'S':
            rotate2 += 1
            rotate0 -= 1
    elif input == 'P':
        if simulateoutput == 'R':
            rotate2 += 1
            rotate0 -= 1
        elif simulateoutput == 'P':
            rotate1 += 1
            rotate2 -= 1
        elif simulateoutput == 'S':
            rotate0 += 1
            rotate1 -= 1
    else:
        if simulateoutput == 'R':
            rotate0 += 1
            rotate1 -= 1
        elif simulateoutput == 'P':
            rotate2 += 1
            rotate0 -= 1
        elif simulateoutput == 'S':
            rotate1 += 1
            rotate2 -= 1
             
    if input == 'R':
        if simulateoutputprime == 'R':
            rotate1prime += 1
            rotate2prime -= 1
        elif simulateoutputprime == 'P':
            rotate0prime += 1
            rotate1prime -= 1
        elif simulateoutputprime == 'S':
            rotate2prime += 1
            rotate0prime -= 1
    elif input == 'P':
        if simulateoutputprime == 'R':
            rotate2prime += 1
            rotate0prime -= 1
        elif simulateoutputprime == 'P':
            rotate1prime += 1
            rotate2prime -= 1
        elif simulateoutputprime == 'S':
            rotate0prime += 1
            rotate1prime -= 1
    else:
        if simulateoutputprime == 'R':
            rotate0prime += 1
            rotate1prime -= 1
        elif simulateoutputprime == 'P':
            rotate2prime += 1
            rotate0prime -= 1
        elif simulateoutputprime == 'S':
            rotate1prime += 1
            rotate2prime -= 1

rotate0 *= 0.95
rotate1 *= 0.95
rotate2 *= 0.95
 
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
    
rotate0prime *= 0.95
rotate1prime *= 0.95
rotate2prime *= 0.95
 
if rotate2prime > rotate0prime and rotate2prime > rotate1prime:
    currentrotationprime += 2
    currentrotationprime %= 3
    temp = rotate0prime
    rotate0prime = rotate2prime
    rotate2prime = rotate1prime
    rotate1prime = temp
elif rotate1prime > rotate0prime and rotate1prime > rotate2prime:
    currentrotationprime += 1
    currentrotationprime %= 3
    temp = rotate0prime
    rotate0prime = rotate1prime
    rotate1prime = rotate2prime
    rotate2prime = temp
    
   

loc = -1
for i in range(1,len(memory)-1):
    thisloc = memory[:-1].rfind(memory[-i:])
    if thisloc != -1:
        loc = thisloc+i
    else:
        break

simulateoutput = ''
if loc != -1:
    prediction = memory[loc]
    if currentrotation == 0:
        if prediction == '1' or prediction == '2' or prediction == '3':
            simulateoutput = 'P'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            simulateoutput = 'S'
        else:
            simulateoutput = 'R'
    elif currentrotation == 1:
        if prediction == '1' or prediction == '2' or prediction == '3':
            simulateoutput = 'S'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            simulateoutput = 'R'
        else:
            simulateoutput = 'P'
    else:
        if prediction == '1' or prediction == '2' or prediction == '3':
            simulateoutput = 'R'
        elif prediction == '4' or prediction == '5' or prediction == '6':
            simulateoutput = 'P'
        else:
            simulateoutput = 'S'

simulateoutputprime = ''
if loc != -1:
    prediction = memory[loc]
    if currentrotationprime == 0:
        if prediction == '1' or prediction == '4' or prediction == '7':
            simulateoutputprime = 'S'
        elif prediction == '2' or prediction == '5' or prediction == '8':
            simulateoutputprime = 'R'
        else:
            simulateoutputprime = 'P'
    elif currentrotationprime == 1:
        if prediction == '1' or prediction == '4' or prediction == '7':
            simulateoutputprime = 'R'
        elif prediction == '2' or prediction == '5' or prediction == '8':
            simulateoutputprime = 'P'
        else:
            simulateoutputprime = 'S'
    else:
        if prediction == '1' or prediction == '4' or prediction == '7':
            simulateoutputprime = 'P'
        elif prediction == '2' or prediction == '5' or prediction == '8':
            simulateoutputprime = 'S'
        else:
            simulateoutputprime = 'R'

 
            
if (randomthresh > rotate0 and randomthresh > rotate0prime) or loc == -1:
    output = random.choice(['R','P','S'])
elif rotate0 > rotate0prime:
    output = simulateoutput
else:
    output = simulateoutputprime
    
previousout = output