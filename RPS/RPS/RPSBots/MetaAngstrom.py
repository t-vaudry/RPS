import random                                                                   
                                                                                
if input == "":                                                                 
    index = {"R": 0, "P": 1, "S": 2}                                            
    counts = [0, 0, 0]                                                          
    names = ("R", "P", "S")                                                     
    beat = (1, 2, 0)                                                            
    R, P, S = 0, 1, 2                                                           
    meta = [(R, P, S), (P, S, R), (S, R, P),                                    
            (R, S, P), (P, R, S), (S, P, R)]                                    
    output = random.choice(names)                                               
    meta_counts_pos = [0 for _ in xrange(6)]                                    
    meta_counts_neg = [0 for _ in xrange(6)]                                    
    m = None                                                                    
else:                                                                           
    k = index[input]                                                            
    if m is not None:                                                           
        for j, x in enumerate(meta):                                            
            n = meta[m][i]                                                      
            if n == beat[k]:                                                    
                meta_counts_neg[j] += 1                                         
            elif k == beat[n]:                                                  
                meta_counts_neg[j] += 1                                         
            meta_counts_neg[j] *= 0.98                                          
            meta_counts_pos[j] *= 0.98                                          
    else:                                                                       
        m = 0                                                                   
    counts[k] += 1                                                              
    for i in xrange(3):                                                         
        counts[i] *= 0.98                                                       
    def r(n):                                                                   
        return random.gammavariate(n + 1, 1)                                    
    sample = [r(n) for n in counts]                                             
    meta_sample = [r(a) - r(b) for a, b in zip(meta_counts_pos,                 
                                               meta_counts_neg)]                
    expected_values = [sample[2] - sample[1],                                   
                       sample[0] - sample[2],                                   
                       sample[1] - sample[0]]                                   
    i = expected_values.index(max(expected_values))                             
    m = meta_sample.index(max(meta_sample))                                     
    output = names[meta[m][i]]