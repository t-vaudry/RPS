import time                                                                  
                                                                             
x = int(time.time())                                                         
                                                                             
def alea():                                                                                                                                     
    global x                                                                    
    x = x * 1103515245 + 12345                                                  
    return ((x >> 16) % 32768) % 3                                              
                                                                                
output = ['R', 'P', 'S'][alea()]