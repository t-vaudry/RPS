import random                                                                   
                                                                                
if input == "":                                                                 
    R, P, S = 0, 1, 2                                                           
    index = {"R": R, "P": P, "S": S}                                            
    name = ("R", "P", "S")                                                      
    beat0 = (P, S, R)                                                           
    beat1 = (S, R, P)                                                           
    beat2 = (R, P, S)                                                           
    beats = [beat0, beat1, beat2]                                               
    counts = [[4 for _ in xrange(3)] for _ in xrange(9)]                        
    meta_counts = [8, 4, 2]                                                     
    m = random.randrange(0, 3)                                                  
    meta = random.randrange(0, 3)                                               
    k = None                                                                    
else:                                                                           
    i = index[input]                                                            
    j = index[output]                                                           
    if k is not None:                                                           
        if j == beat0[i]:                                                       
            meta_counts[meta] += 1                                              
        elif i == beat0[j]:                                                     
            meta_counts[(meta + 2) % 3] += 1                                    
        else:                                                                   
            meta_counts[(meta + 1) % 3] += 1                                    
        counts[k][i] += 2                                                       
    k = 3 * i + j                                                               
    ns = counts[k]                                                              
    t = sum(ns)                                                                 
    r = random.randint(0, t)                                                    
    p = 0                                                                       
    for m, n in enumerate(ns):                                                  
        p += n                                                                  
        if r <= p:                                                              
            break                                                               
    t = sum(meta_counts)                                                        
    r = random.randint(0, t)                                                    
    p = 0                                                                       
    for meta, n in enumerate(meta_counts):                                      
        p += n                                                                  
        if r <= p:                                                              
            break                                                               
output = name[beats[meta][m]]