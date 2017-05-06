import time                                                                  
                                                                                                                                                
if input == "":                                                              
    x = int(time.time())                                                     
else:                                                                        
    x = x * 1103515245 + 12345                                               
                                                                             
output = ["R", "P", "S"][(x << 16) % 3]