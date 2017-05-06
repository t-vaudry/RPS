from random import randint



class treePredictor():
    def __init__(self):
        self.choices = ['R', 'P', 'S']
        self.prevchoice = None
        self.prevres = None
        self.dataarr =[[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] #choice, result, nextmove
        
        #self.gameMat = np.zeros((3,3), dtype=np.uint8)
        self.gameMat = [0,0,0]
        self.gameMat[0]=[1, 0, 2]
        self.gameMat[1]=[2, 1, 0]
        self.gameMat[2]=[0, 2, 1]
        #self.gameMat = []
        #self.gameMat.append([1, 0, 2])
        #self.gameMat.append([2, 1, 0])
        #self.gameMat.append([0, 2, 1])
        self.beatMat=[1,2,0]
    def gameRes(self, c1, c2):
        i1 = self.choices.index(c1)
        i2 = self.choices.index(c2)
        #print i1, i2
        return self.gameMat[i1][i2]
    def predict(self):
        if self.prevchoice is None or self.prevres is None:
            return self.choices[randint(0,2)]
        arr=self.dataarr[self.prevchoice, self.prevres]
        predictedchoice = arr.index(max(arr))#np.argmax(self.dataarr[self.prevchoice, self.prevres])
        choice = self.beatMat[predictedchoice]
        return self.choices[choice]
    #def choice2ind(self, c):
    #    return np.where(choices==c)
    def store(self, c, c2):
        i1 = self.choices.index(c)
        if not (self.prevchoice is None or self.prevres is None):
            self.dataarr[self.prevchoice, self.prevres, i1]+=1
            #i2 = self.choices.index(c2)
            #res = self.gameRes(c,c2)
        self.prevchoice = i1
        self.prevres = self.gameRes(c,c2)
        
tp = treePredictor()

output = tp.predict()
if input != '':
    tp.store(input, output)