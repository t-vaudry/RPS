import random
	
if input == "":	
	opp_moves=[]
	my_moves=[]
	
	winner={'R': 'P', 'P': 'S', 'S': 'R'} 
	follows={}   

	output=random.choice(['P', 'S', 'R'])
        print output
		
else:
	opp_moves.append(input)
	my_moves.append(output)	
    
	if len(opp_moves)<5:
	        output=random.choice(['P', 'S', 'R'])
    
	else:
		i=len(opp_moves)-5    
      
		x=opp_moves[i]  
		y=opp_moves[i+1] 
		z=opp_moves[i+2]
		w=opp_moves[i+3]
		v=opp_moves[i+4]
			
		if (x,y,z,w) not in follows:
			follows[(x,y,z,w)]={}         
			
		if v not in follows[(x,y,z,w)]:
			follows[(x,y,z,w)][v]=1
		else:
			follows[(x,y,z,w)][v]+=1   
		
		last=opp_moves[-1]
		one_before_last=opp_moves[-2]
		two_before_last=opp_moves[-3]
		three_before_last=opp_moves[-4]
			
		the_end=(three_before_last,two_before_last, one_before_last, last)
			
		if the_end in follows:
			maxim=0
			solution=-1
				
			for i in follows[the_end]:
				if follows[the_end][i]>maxim:
					maxim=follows[the_end][i]
					solution=i
					
			output=winner[solution] 		
		else:
			output=random.choice(['P', 'S', 'R'])