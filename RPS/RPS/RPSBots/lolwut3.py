import random


#def metastrategy1(S,R,P):     
#    if S == max(S,R,P):
#        output = anti["S"]
#    elif P == max(S,R,P):
#        output = anti["P"]
#    elif R == max(S,R,P):
#        output = anti["R"]
#    return output
#
#def metastrategy2(S,R,P):
#    if S == max(S,R,P):
#        output = anti[anti["S"]]
#    elif P == max(S,R,P):
#        output = anti[anti["P"]]
#    elif R == max(S,R,P):
#        output = anti[anti["R"]]
#    return output

if input == "":
    combine = { 'PP': '1', 
            'PR': '2', 
            'PS': '3',
            'RP': '4',
            'RS': '5',
            'RR': '6',
            'SS': '7',
            'SP': '8',
            'SR': '9',}
            
    split = {'1':'PP', 
              '2':'PR', 
              '3':'PS',
              '4':'RP',
              '5':'RS',
              '6':'RR',
              '7':'SS',
              '8':'SP',
              '9':'SR',}   
              
    anti = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    sequence = ""
    output = random.choice(['R','P','S'])
   
else:
    if len(sequence) % 10 == 0:
        output = random.choice(['R','P','S'])
    else:
        choices = []    
        
        if output != "":
            sequence += combine[output + input]
    
        for number in range(min(20, len(sequence)-1), 7, -1):
            pattern = sequence[-number:]
            index = sequence.find(pattern, 0, len(sequence) - 1)
            if index != -1:
                index += number
                choice = sequence[index]
                choices.append(split[choice][1])
            else:
                pass
        
        S = 0
        R = 0
        P = 0
                
        if len(choices) != 0:
            for choice in choices:
                if choice == 'S':
                    S += 1
                elif choice == 'P':
                    P += 1
                else:
                    R += 1
            
            #conditions if-else for metastrategies
            metastrategyOne = False        
            
            for x in range(-1, -10, -1):
                if split[sequence[index]][2] != anti[split[sequence[index]][1]]:
                    metastrategyOne = True
            
            if metastrategyOne == True:
                #output = metastrategy1(S, R, P)
                if S == max(S,R,P):
                    output = anti['S']
                elif P == max(S,R,P):
                    output = anti['P']
                elif R == max(S,R,P):
                    output = anti['R']
                #return output
            else:
                #output = metastrategy2(S, R, P)
                if S == max(S,R,P):
                    output = anti[anti['S']]
                elif P == max(S,R,P):
                    output = anti[anti['P']]
                elif R == max(S,R,P):
                    output = anti[anti['R']]
                #return output
            
        else:
            output = random.choice(['R','P','S'])