KAMEN, SKARJE, PAPIR = 0, 1, 2

class Player:

    def __init__(self):
        self.name = "Jure Slak"
        self.history = "";
        self.count = [1, 1, 1]
        self.beat = {"R": PAPIR, "P": SKARJE, "S": KAMEN}
        self.leg = {"R": KAMEN, "P": PAPIR, "S": SKARJE}

    def play(self):
        b = True
        count = [0,0,0]
        for i in xrange(len(self.history)/2, 3, -1):
            count = [0,0,0]
            j = len(self.history)                                                                                                                                                  
            while j != -1:                                                                                                                                                         
                j = rfind(a[i:], j)                                                                                                                                                
                if j != -1:                                                                                                                                                        
                    count[self.leg[a[j+len(self.history)-i]]] += 1                                                                                                                 
                    b = False                                                                                                                                                      
            if not b: break                                                                                                                                                        
                                                                                                                                                                                   
        if count != [0,0,0]:                                                                                                                                                           
            return count.index(max(count))                                                                                                                                                 
                                                                                                                                                                                   
                                                                                                                                                                                   
        return self.w_choice(zip([PAPIR,KAMEN,SKARJE],map(lambda x: float(x)/sum(self.count), self.count)))                                                                        
                                                                                                                                                                                   
    def other(self, sign):                                                                                                                                                         
        assert 0 <= sign <= 2                                                                                                                                                      
        self.history += str(sign);                                                                                                                                                 
        self.count[sign] += 1

    def __str__(self):
        return ""+\
               "Player Jure Slak\
"+\
               "History: {0}\
".format(self.history[len(self.history)-50:])+\
               "Count: K: {1}   S: {2}    P: {3}\
".format(*self.count)

    def __repr__(self): return str(self)

    def w_choice(self, lst):
        import random
        n = random.uniform(0, 1)
        for item, weight in lst:
                if n < weight: break
                n -= weight
        return item

p = Player()

invleg = {'R': KAMEN, "S": SKARJE, "P": PAPIR}

if input:
    p.other(invleg[input])

output = "RSP"[p.play()]