from __future__ import division
import random as rnd

def checkGame(x, y): #x is my program, y is opponent program
    if x == 'R' and y == 'S' or x == 'P' and y == 'R' or x == 'S' and y == 'P':
        return 1
    elif x == y:
        return 0
    else:
        return -1
####################VARIABLES USED IN PROGRAM########################
k0 = .99
k1 = .97  #exponential factor

RPS_dic = 'RPS'

if input == '':
    x_list = [] #x_list[i] denotes throw at time -i. i = 0 denotes most recent throw
    y_list = []
    
    switch = 0

    for i in range(0,2):
        x_list.append( RPS_dic[rnd.randint(0,2)] )
        y_list.append( RPS_dic[rnd.randint(0,2)] )

r_count, p_count, s_count = 0, 0, 0
######################################################################
#compute EMA for opponent history if switch == 0
if switch == 0:
    
    for i in range( 0, len(y_list)-2 ):
        
        if y_list[i+1] == y_list[0] and y_list[i+2] == y_list[1]:
            if y_list[i] == 'R':
                r_count += k0**i
                
            elif y_list[i] == 'P':
                p_count += k0**i
        
            elif y_list[i] == 'S':
                s_count += k0**i

elif switch == 1:
    
    for i in range( 0, len(y_list)-1 ):
        
        if y_list[i+1] == y_list[0] and x_list[i+1] == x_list[0]:
            if y_list[i] == 'R':
                r_count += k1**i
                
            elif y_list[i] == 'P':
                p_count += k1**i
        
            elif y_list[i] == 'S':
                s_count += k1**i

pay_distribution = [s_count - p_count, r_count - s_count, p_count - r_count]

if pay_distribution[0] == 0 and pay_distribution[1] == 0 and pay_distribution[2] == 0:
    output = RPS_dic[ rnd.randint(0,2) ]

else:
    output = RPS_dic[ pay_distribution.index( max(pay_distribution) ) ]

temp = checkGame(output, input)

if temp ==  1:
    switch = 0
    
elif temp == 0:
    switch = 0

elif temp == -1:
    switch = 1

x_list.insert(0, output)
    
y_list.insert(0, input)