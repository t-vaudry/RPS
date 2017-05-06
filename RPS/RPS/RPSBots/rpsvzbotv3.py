from random import randint



class treePredictor():
    def __init__(self):
        self.choices = ['R', 'P', 'S']
        self.prevchoice = None #computer move
        self.prevmove = None #my move
        self.prevres = None
        self.dataarr =[[0 for _ in range(3)] for _ in range(3)] #result, roll
        
        #self.gameMat = np.zeros((3,3), dtype=np.uint8)
        #self.gameMat = [0,0,0]
        #self.gameMat[0]=[1, 0, 2]
        #self.gameMat[1]=[2, 1, 0]
        #self.gameMat[2]=[0, 2, 1]
        self.gameMat = []
        self.gameMat.append([1, 0, 2])
        self.gameMat.append([2, 1, 0])
        self.gameMat.append([0, 2, 1])
        self.beatMat=[1,2,0]
        
        self.rollMat = []
        self.rollMat.append([0, 1, 2])
        self.rollMat.append([2, 0, 1])
        self.rollMat.append([1, 2, 0])
        
        self.losecount=0;
        self.playrand=False
    def gameRes(self, c1, c2):
        i1 = self.choices.index(c1)
        i2 = self.choices.index(c2)
        #print i1, i2
        return self.gameMat[i1][i2]
    def getRoll(self, c1, c2):
        i1 = self.choices.index(c1)
        i2 = self.choices.index(c2)
        return self.rollMat[i1][i2]
    def getRollbyInd(self, i1, i2):
        #i1 = self.choices.index(c1)
        #i2 = self.choices.index(c2)
        return self.rollMat[i1][i2]
    
    def rollInd(self,i1, inc):
        #i1 = self.choices.index(c)
        row = self.rollMat[i1]
        ind = row.index(inc)
        return ind
        
    def predict(self):
        if self.prevchoice is None or self.prevres is None:
            return self.choices[randint(0,2)]
        arr=self.dataarr[self.prevres]
        #print arr
        predictedroll = arr.index(max(arr))
        predictedchoice = self.rollInd(self.prevchoice, predictedroll)
        #print "predicted: ", predictedchoice, self.choices[predictedchoice]
        choice = self.beatMat[predictedchoice]
        if self.playrand:
            self.playrand=False
            #print "random choice"
            choice = randint(0,2)
        #print "made choice: ", choice, self.choices[choice]
        return self.choices[choice]
    #def choice2ind(self, c):
    #    return np.where(choices==c)
    def store(self, c):
        
        i1 = self.choices.index(c)
        #print "got: ", i1, c
        if not (self.prevchoice is None or self.prevres is None):
            roll = self.getRollbyInd(self.prevchoice, i1)
            #print "res, roll", self.prevres, roll
            #self.dataarr[self.prevres]=[0,0,0]
            self.dataarr[self.prevres][roll]+=1
            #print self.dataarr
            #i2 = self.choices.index(c2)
            #res = self.gameRes(c,c2)
        #print self.dataarr
        self.prevchoice = i1
        self.prevres = self.gameRes(c,self.prevmove)
        
        #if self.prevres == 2:
        #    self.losecount+=1
        #else:
        #    self.losecount=0
            
        #if(self.losecount==2):
            #print "rest lc"
        #    self.losecount=0
        #    self.playrand=True
            #self.dataarr =[[0 for _ in range(3)] for _ in range(3)]
                
    #def __del__(self):
    #    print self.dataarr



if input == '':
    #output='R'
    tp = treePredictor()
    output = tp.predict()
    tp.prevmove = output
else:
    #output='R'
    tp.store(input)
    output = tp.predict()