if input == "":                                                                 
               
    import collections                                                                 
    import random                                                               
                                                                                
    R, P, S = 0, 1, 2                                                           
    index = {"R": R, "P": P, "S": S}                                            
    name = ("R", "P", "S")                                                      
    beat = (P, S, R)                                                            
    beaten = (S, R, P)                                                          
                                                                                
    third = 1.0 / 3.0                                                           
                                                                                
    class MarkovTree:                                                           
        def __init__(self):                                                     
            self.weight   = 0.0                                                 
            self.counts   = [0 for _ in xrange(3)]                              
            self.children = None                                                
        def node_prediction(self, x):                                           
            return (self.counts[x] + third) / (sum(self.counts) + 1.0)          
        def expectation(self, x):                                               
            return self.node_prediction(x) - self.node_prediction(beaten[x])    
        def update(self, h, x):                                                 
            for y in h:                                                         
                self.weight += self.expectation(x)                              
                self.counts[x] += 1                                             
                if self.children is None:                                       
                    self.children = [None for _ in xrange(3)]                   
                if self.children[y] is None:                                    
                    child = MarkovTree()                                        
                    child.counts[x] = 1                                         
                    self.children[y] = child                                    
                    return                                                      
                self = self.children[y]                                         
        def predict(self, h):                                                   
            counts = [0, 0, 0]                                                  
            for y in h:                                                         
                k = self.weight / (sum(self.counts) + 1.0)                      
                for i in xrange(3):                                             
                    counts[i] += k * (self.counts[i] + third)                   
                if self.children is None or self.children[y] is None:           
                    break                                                       
                self = self.children[y]                                         
            return counts                                                       
                                                                                
    model = MarkovTree()                                                        
                                                                                
    history = collections.deque([])                                             
                                                                                
else:                                                                           
                                                                                
    i = index[input]                                                            
    j = index[output]                                                           
                                                                                
    model.update(history, i)                                                    
                                                                                
    history.appendleft(i)                                                       
    history.appendleft(j)                                                       
                                                                                
counts = model.predict(history)                                                 
scores = [0 for _ in xrange(3)]                                                 
                                                                                
for i in xrange(3):                                                             
    r = random.uniform(0, sum(counts))                                          
    n = 0                                                                       
    for j in xrange(3):                                                         
        n += counts[j]                                                          
        if n >= r:                                                              
            break                                                               
    scores[beat[j]] += 1                                                        
    scores[beaten[j]] += 1                                                      
                                                                                
output = name[scores.index(max(scores))]