import time                                                                  
                                                                             
class Alea:                                                                  
    def __init__(self):                                                      
        self.actual = int(time.time())                                       
    def alea(self):                                                          
        self.actual = self.actual * 1103515245 + 12345                       
        return (((self.actual >> 16) % 32768) % 3)                                                                                              
                                                                             
aleatorios = Alea()                                                          
                                                                             
output = ['R', 'P', 'S'][aleatorios.alea()]