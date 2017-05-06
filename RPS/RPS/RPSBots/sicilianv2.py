import random
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
    strategy=[0,1,2]
    used=[1,1,1]
    score=[0,0,0]
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else: 
	if round >1 :
	   str=output+input
	   val=result[str]
	   strategy[last_str]+=val

        for index, xi in enumerate(strategy):
           for index1, yi in enumerate(used):
             if index == index1:
                 score[index]=xi/yi

        
	max_value = max(score)
	max_index = score.index(max_value)

	if max_index==0:
	    response = {'R': 'R', 'P': 'P','S' : 'S'}
            output=response[input]
            used[0]+=1
	    last_str=0
	elif max_index==1:
	    response = {'R': 'P', 'P': 'S','S' : 'R'}
            output=response[input]
            used[1]+=1
	    last_str=1
	else:
	    response = {'R': 'S', 'P': 'R','S' : 'P'}
            output=response[input]
            used[2]+=1
	    last_str = 2
    
	round+=1