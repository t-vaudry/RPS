import time                                                                  
                                                                             
if input == "":                                                              
    actual = int(time.time())                                                
else:                                                                        
    actual = actual * 1103515245 + 12345                                     
                                                                             
output = ["R", "P", "S"][int(3*(float((actual << 16)%32767)/32767))]