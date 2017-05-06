import random
SWITCH=25
def most_common(l):
    max = 0
    maxitem = None
    for x in set(l):
        count =  l.count(x)
        if count > max:
            max = count
            maxitem = x
    return maxitem
#################################
if input == "": # initialize variables for the first round
    output=random.choice(['R','P','S'])
    round=0
    last_str=0
    str=''
    strategy=[0.3,0.6,0.9]
    out=['','','']
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else: 
	if round >1 :
           for i in range(0,3):
                  str=out[i]+input
                  strategy[i]+=result[str]

	if round<SWITCH:
		max_index=random.choice([0,1,2])
	else:
		max_value = max(strategy)
		max_index = strategy.index(max_value)
        
        response = {'R': 'R', 'P': 'P','S' : 'S'}
        out[0]=response[input]
        response = {'R': 'P', 'P': 'S','S' : 'R'}	
        out[1]=response[input]	
        response = {'R': 'S', 'P': 'R','S' : 'P'}
        out[2]=response[input]

	if max_index==0:
	    response = {'R': 'R', 'P': 'P','S' : 'S'}
	    last_str=0
	elif max_index==1:
	    response = {'R': 'P', 'P': 'S','S' : 'R'}
	    output=response[input]
            last_str=1
	else:
	    response = {'R': 'S', 'P': 'R','S' : 'P'}
	    output=response[input]
	    last_str = 2

	round+=1