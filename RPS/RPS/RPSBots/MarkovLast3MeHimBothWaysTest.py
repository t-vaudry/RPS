import random
	
if input == "":	
	opp_moves=[]
	my_moves=[]
	
	winner={'R': 'P', 'P': 'S', 'S': 'R'} 
	follows={}   
	my_next={}

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
		d=my_moves[i+3]
				
		his_last=opp_moves[-1]
    		one_before_his_last=opp_moves[-2]
                two_before_his_last=opp_moves[-3]

    		my_last=my_moves[-1]
    		one_before_my_last=my_moves[-2]
                two_before_my_last=my_moves[-3]

    		the_end=(two_before_his_last,two_before_my_last,one_before_his_last,one_before_my_last, his_last, my_last)
				
		if (x,a,y,b,z,c) not in my_next:
            		my_next[(x,a,y,b,z,c)]={}         
        
        	if d not in my_next[(x,a,y,b,z,c)]:
            		my_next[(x,a,y,b,z,c)][d]=1
        	else:
            		my_next[(x,a,y,b,z,c)][d]+=1     		
		
		his_guess=None
		
		if the_end in my_next:
			maxim=0
			solution=-1
				
			for i in my_next[the_end]:
				if my_next[the_end][i]>maxim:
					maxim=my_next[the_end][i]
					solution=i
					
			his_guess=solution			
        
        	if (x,a,y,b,z,c) not in follows:
            		follows[(x,a,y,b,z,c)]={}         
        
        	if w not in follows[(x,a,y,b,z,c)]:
            		follows[(x,a,y,b,z,c)][w]=1
        	else:
            		follows[(x,a,y,b,z,c)][w]+=1       
			
		if the_end in follows:
			maxim=0
			solution=-1
				
			for i in follows[the_end]:
				if follows[the_end][i]>maxim:
					maxim=follows[the_end][i]
					solution=i
					
			my_guess=winner[solution]

			if his_guess==my_guess:
                                lis=['P', 'S', 'R']
                                random.shuffle(lis)
				for x in lis:
					if x!=my_guess:
						output=x
						break
			else:
				output=my_guess
		else:
			output=random.choice(['P', 'S', 'R'])