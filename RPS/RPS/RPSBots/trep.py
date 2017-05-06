if input == "": # initialize variables for the first round
   import random
	
   left = [2,4,6,8,10,12,14,0,0,0,0,0,0,0,0]
   right = [3,5,7,9,11,13,15,0,0,0,0,0,0,0,0]
   split = ["S","S","R","R","R","R","P","R","R","P","S","P","R","S","P"]
   var = [9,7,9,2,4,7,7,0,0,0,0,0,0,0,0]
	
   n_nodes = 0
   lam = 0.2
   def update_node(probs,s):
      probs[0] = probs[0]*(1-lam)
      probs[1] = probs[1]*(1-lam)
      probs[2] = probs[2]*(1-lam)
      if s == "R":
         probs[0]=probs[0]+lam
      if s == "P":
         probs[1]=probs[1]+lam
      if s == "S":
         probs[2]=probs[2]+lam

      s = probs[0]+probs[1]+probs[2]
      probs[0] = probs[0]/s
      probs[1] = probs[1]/s
      probs[2] = probs[2]/s
      return probs;
      
   def sample_rps(probs):
      u = random.uniform(0,1)
      p2 = probs[0]+probs[1]
      if u <= probs[0]:
         return "R"
      elif u <= p2:
         return "P"
      return "S";

   for i in range(0,len(var)):
      if var[i] == 0:
         n_nodes = n_nodes+1
   #n_nodes = 8
   
   nodes_num = [0]
   for i in range(1,len(var)):
   	nodes_num.append(0)
   
   nodes_cur = [[1.0/3,1.0/3,1.0/3]]
   
   for i in range(1,n_nodes):
      nodes_cur.append([1.0/3,1.0/3,1.0/3])
	
   n_var = 5
   
   x = [sample_rps([1.0/3,1.0/3,1.0])]
   for i in range(1,2*n_var):
      x.append(sample_rps([1.0/3,1.0/3,1.0]))
 
   output = x[4]
else:
    x1 = [x[index] for index in range(1,n_var)]
    x2 = [x[index] for index in range(n_var+1,2*n_var)] 
    x1.append(output)
    x2.append(input)
    x = x1+x2


    not_pred = True
    i = 0
    while not_pred:
        if x[(var[i]-1)] == split[i]:
            i = left[i]-1
        else:
            i = right[i]-1
        if var[i] == 0:
            not_pred = False

    nr = nodes_num[i]

    pred = sample_rps(nodes_cur[nr])
    output = pred