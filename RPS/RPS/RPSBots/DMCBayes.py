if input == "":                                                                 
                                                                                
    import random                                                               
                                                                                
    class MarkovChain:                                                          
        def __init__(self, counts = None):                                      
            self.visits = 0                                                     
            if counts is None:                                                  
                self.counts = [0 for _ in xrange(3)]                            
            else:                                                               
                self.counts = counts                                            
            self.children = None                                                
                                                                                
        def split_edge(self, i):                                                
            old = self.children[i]                                              
            new = MarkovChain(old.counts)                                       
            self.children[i] = new                                              
            new.children = old.children                                         
                                                                                
        def transition(self, i, j):                                             
            self.visits += 1                                                    
            self.counts[i] += 1                                                 
            for i in xrange(3):                                                 
                self.counts[i] *= 0.99                                          
            k = 3 * i + j                                                       
            if self.children[k].visits >= 9:                                    
                self.split_edge(k)                                              
            return self.children[k]                                             
                                                                                
    R, P, S = 0, 1, 2                                                           
    index = {"R": R, "P": P, "S": S}                                            
    name = ["R", "P", "S"]                                                      
                                                                                
    l = 3                                                                       
                                                                                
    nodes = [[MarkovChain() for _ in xrange(9)] for _ in xrange(l)]             
                                                                                
    for i in xrange(l):                                                         
        children = nodes[(i + 1) % l]                                           
        for j in xrange(9):                                                     
            nodes[i][j].children = children                                     
                                                                                
    model = MarkovChain()                                                       
    model.children = nodes[0]                                                   
                                                                                
else:                                                                           
    i = index[input]                                                            
    j = index[output]                                                           
    model = model.transition(i, j)                                              
                                                                                
counts = model.counts                                                           
                                                                                
sample = [random.gammavariate(n + 1, 1) for n in counts]                        
expected_values = [sample[2] - sample[1],                                       
                   sample[0] - sample[2],                                       
                   sample[1] - sample[0]]                                       
j = 0                                                                           
e = 0                                                                           
for i, x in enumerate(expected_values):                                         
    if x >= e:                                                                  
        j = i                                                                   
        e = x                                                                   
output = name[j]