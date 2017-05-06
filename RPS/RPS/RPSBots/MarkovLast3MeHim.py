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
    
	if len(opp_moves)<4:
	        output=random.choice(['P', 'S', 'R'])
    
	else:
		i=len(opp_moves)-4

		x=opp_moves[i]  
        	y=opp_moves[i+1] 
        	z=opp_moves[i+2]
                w=opp_moves[i+3]
        
        	a=my_moves[i]
        	b=my_moves[i+1]
                c=my_moves[i+2]
        
        	if (x,a,y,b,z,c) not in follows:
            		follows[(x,a,y,b,z,c)]={}         
        
        	if w not in follows[(x,a,y,b,z,c)]:
            		follows[(x,a,y,b,z,c)][w]=1
        	else:
            		follows[(x,a,y,b,z,c)][w]+=1   
    
    		his_last=opp_moves[-1]
    		one_before_his_last=opp_moves[-2]
                two_before_his_last=opp_moves[-3]

    		my_last=my_moves[-1]
    		one_before_my_last=my_moves[-2]
                two_before_my_last=my_moves[-3]

    		the_end=(two_before_his_last,two_before_my_last,one_before_his_last,one_before_my_last, his_last, my_last)
			
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