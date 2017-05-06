import random
SWITCH=25
############################
def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])
#################################
if input == "": # initialize variables for the first round
    output=random.choice(['R','P','S'])
    round=0
    arr={'R':0,'P':0,'S':0}
    #he now, me next
    probabilities={'RR':1,'RP':1,'RS':1,'PR':1,'PP':1,'PS':1,'SR':1,'SP':1,'SS':1}
    wins={'R':'P','P':'S','S':'R'}
else: 
	if round >1 :
           temp_str= last_input + wins[input]  
           probabilities[temp_str]+=1 
             
	if round<SWITCH:
		output=random.choice(['R','P','S'])
	else:
                for temp in ['R','P','S']:
                     temp_str = input + temp
                     arr[temp]= probabilities[temp_str]
                output=max(arr, key=arr.get) 
                     
	round+=1
        last_input=input