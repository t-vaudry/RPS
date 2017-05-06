from random import randint



class treePredictor():
    def __init__(self):
        self.choices = ['R', 'P', 'S']
        self.prevchoice = None
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
    
    def rollInd(c, inc):
        i1 = self.choices.index(c1)
        row = self.rollMat[i1]
        ind = row.index(inc)
        return self.choices[ind]
        
    def predict(self):
        if self.prevchoice is None or self.prevres is None:
            return self.choices[randint(0,2)]
        arr=self.dataarr[self.prevres]
        #print arr
        predictedchoice = arr.index(max(arr))#np.argmax(self.dataarr[self.prevchoice, self.prevres])
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
    def store(self, c, c2):
        
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
        self.prevres = self.gameRes(c,c2)
        
        if self.prevres == 2:
            self.losecount+=1
        else:
            self.losecount=0
            
        if(self.losecount==3):
            #print "rest lc"
            self.losecount=0
            self.playrand=True
            #self.dataarr =[[0 for _ in range(3)] for _ in range(3)]
                
    #def __del__(self):
    #    print self.dataarr



if input == '':
    tp = treePredictor()
    output = tp.predict()
else:
    output = tp.predict()    
    tp.store(input, output)