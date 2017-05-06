#author blue-tomato

if input == '':

    import random

    beat = {'R':'P','P':'S','S':'R'}
    lose = {'R':'S','P':'R','S':'P'}

    class RfindPairs:
        def __init__(self):
            self.memory = ''
        def run(self, input, lastoutput):

            self.memory += {('R','R'):'1',('R','P'):'2',('R','S'):'3', \
                            ('P','R'):'4',('P','P'):'5',('P','S'):'6', \
                            ('S','R'):'7',('S','P'):'8',('S','S'):'9'}[(input,lastoutput)]
            loc = -1
            for i in range(1,min(51,len(self.memory))):
                thisloc = self.memory[:-1].rfind(self.memory[-i:])
                if thisloc == -1:
                    break
                else:
                    loc = thisloc+i
            if loc == -1:
                return 'X'
            else:
                prediction = self.memory[loc]
                return {'1':'P','2':'P','3':'P','4':'S','5':'S','6':'S','7':'R','8':'R','9':'R'}[prediction]
                
    class RfindInput:

        def __init__(self):
            self.memory = ''
            
        def run(self, input, lastoutput):
            self.memory += input
            loc = -1
            for i in range(1,min(51,len(self.memory))):
                thisloc = self.memory[:-1].rfind(self.memory[-i:])
                if thisloc == -1:
                    break
                else:
                    loc = thisloc+i
            if loc == -1:
                return 'X'
            else:
                prediction = self.memory[loc]
                return beat[prediction]
                
    class Expectation:
        
        def __init__(self):
            self.numR = 0
            self.numP = 0
            self.numS = 0
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1
            if input == 'P':
                self.numP += 1
            if input == 'S':
                self.numS += 1
                
            scoreR = self.numS - self.numP
            scoreP = self.numR - self.numS
            scoreS = self.numP - self.numR
                
            if scoreR > scoreP and scoreR >= scoreS:
                return 'R'
            if scoreP > scoreS and scoreP >= scoreR:
                return 'P'
            if scoreS > scoreR and scoreS >= scoreP:
                return 'S'
            return 'X'
            
    class ExpectationCut:
        
        def __init__(self, cut):
            self.numR = 0
            self.numP = 0
            self.numS = 0
            self.cut = cut
            self.pipe = ''
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1
            if input == 'P':
                self.numP += 1
            if input == 'S':
                self.numS += 1
                
            self.pipe += input
            if self.pipe > self.cut:
                uninput = self.pipe[0]
                if uninput == 'R':
                    self.numR -= 1
                if uninput == 'P':
                    self.numP -= 1
                if uninput == 'S':
                    self.numS -= 1
                self.pipe = self.pipe[1:]
                
            scoreR = self.numS - self.numP
            scoreP = self.numR - self.numS
            scoreS = self.numP - self.numR
                
            if scoreR > scoreP and scoreR >= scoreS:
                return 'R'
            if scoreP > scoreS and scoreP >= scoreR:
                return 'P'
            if scoreS > scoreR and scoreS >= scoreP:
                return 'S'
            return 'X'
            
    class ExpectationDecay:
        
        def __init__(self, decay):
            self.numR = 0.0
            self.numP = 0.0
            self.numS = 0.0
            self.decay = decay
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1.0
            if input == 'P':
                self.numP += 1.0
            if input == 'S':
                self.numS += 1.0
                
            self.numR *= self.decay
            self.numP *= self.decay
            self.numS *= self.decay
                
            scoreR = self.numS - self.numP
            scoreP = self.numR - self.numS
            scoreS = self.numP - self.numR
                
            if scoreR > scoreP and scoreR >= scoreS:
                return 'R'
            if scoreP > scoreS and scoreP >= scoreR:
                return 'P'
            if scoreS > scoreR and scoreS >= scoreP:
                return 'S'
            return 'X'
            
    class Frequency:
        
        def __init__(self):
            self.numR = 0
            self.numP = 0
            self.numS = 0
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1
            if input == 'P':
                self.numP += 1
            if input == 'S':
                self.numS += 1
                
            if self.numR > self.numP and self.numR >= self.numS:
                return 'R'
            if self.numP > self.numS and self.numP >= self.numR:
                return 'P'
            if self.numS > self.numR and self.numS >= self.numP:
                return 'S'
            return 'X'
            
    class FrequencyCut:
        
        def __init__(self, cut):
            self.numR = 0
            self.numP = 0
            self.numS = 0
            self.cut = cut
            self.pipe = ''
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1
            if input == 'P':
                self.numP += 1
            if input == 'S':
                self.numS += 1
                
            self.pipe += input
            if self.pipe > self.cut:
                uninput = self.pipe[0]
                if uninput == 'R':
                    self.numR -= 1
                if uninput == 'P':
                    self.numP -= 1
                if uninput == 'S':
                    self.numS -= 1
                self.pipe = self.pipe[1:]
                
            if self.numR > self.numP and self.numR >= self.numS:
                return 'R'
            if self.numP > self.numS and self.numP >= self.numR:
                return 'P'
            if self.numS > self.numR and self.numS >= self.numP:
                return 'S'
            return 'X'
            
    class FrequencyDecay:
        
        def __init__(self, decay):
            self.numR = 0.0
            self.numP = 0.0
            self.numS = 0.0
            self.decay = decay
            
        def run(self, input, lastoutput):
            if input == 'R':
                self.numR += 1.0
            if input == 'P':
                self.numP += 1.0
            if input == 'S':
                self.numS += 1.0
                
            self.numR *= self.decay
            self.numP *= self.decay
            self.numS *= self.decay
                
            if self.numR > self.numP and self.numR >= self.numS:
                return 'R'
            if self.numP > self.numS and self.numP >= self.numR:
                return 'P'
            if self.numS > self.numR and self.numS >= self.numP:
                return 'S'
            return 'X'
            
    class MetaRotationRfind:

        def __init__(self, child):
            self.child = child
            self.r0prev = 'X'
            self.memory = ''
            
        def run(self, input, lastoutput):
            
            if self.r0prev == beat[input]:
                self.memory += 'A'
            elif self.r0prev == input:
                self.memory += 'B'
            elif self.r0prev == lose[input]:
                self.memory += 'C'
            
            r0 = self.child.run(input, lastoutput)
            self.r0prev = r0
            if r0 == 'X':
                return 'X'
                
            loc = -1
            for i in range(1,min(51,len(self.memory))):
                thisloc = self.memory[:-1].rfind(self.memory[-i:])
                if thisloc == -1:
                    break
                else:
                    loc = thisloc+i
            if loc == -1:
                return 'X'
                
            prediction = self.memory[loc]
            
            if prediction == 'A':
                return r0
            if prediction == 'B':
                return beat[r0]
            if prediction == 'C':
                return lose[r0]
                
    class Flip:
        
        def __init__(self, child):
            self.child = child
            
        def run(self, input, lastoutput):
            return self.child.run(lastoutput, input)
            
    class MetaDoubleRfind:

        def __init__(self, child, flipchild):
            
            self.rotpat = MetaRotationRfind(child)
            self.rotpatlastguess = ''
            self.rotpatscore = 0.0
            self.rotpatflip = MetaRotationRfind(flipchild)
            self.rotpatfliplastguess = ''
            self.rotpatflipscore = 0.0
            
            
        def run(self, input, lastoutput):
        
            if input != '':
            
                if self.rotpatlastguess == beat[input]:
                    self.rotpatscore += 1.0
                elif self.rotpatlastguess == lose[input]:
                    self.rotpatscore -= 1.0
                self.rotpatscore *= 0.95
                
                if self.rotpatfliplastguess == beat[input]:
                    self.rotpatflipscore += 1.0
                elif self.rotpatfliplastguess == lose[input]:
                    self.rotpatflipscore -= 1.0
                self.rotpatflipscore *= 0.95
                
            rotpatout = self.rotpat.run(input, lastoutput)
            rotpatflipout = self.rotpatflip.run(input, lastoutput)
            
            self.rotpatlastguess = rotpatout
            self.rotpatfliplastguess = rotpatflipout
            
            if self.rotpatscore >= self.rotpatflipscore:
                return rotpatout
            else:
                return rotpatflipout
                
    class MetaMerge:

        def __init__(self, AIList):
            self.AIList = len(AIList)*[0]
            self.AIOffset = len(AIList)*[0.0]
            self.AIGuess = len(AIList)*['']
            self.AIScores = len(AIList)*[0.0]
            for i in range(0,len(AIList)):
                (offset,AI) = AIList[i]
                self.AIList[i] = AI
                self.AIOffset[i] = offset
                self.AIScores[i] = offset
            
        def run(self, input, lastoutput):
            for i in range(0,len(self.AIList)):
                if self.AIGuess[i] == beat[input]:
                    self.AIScores[i] += 1.0
                elif self.AIGuess[i] == lose[input]:
                    self.AIScores[i] -= 1.0
                self.AIScores[i] = ((self.AIScores[i]-self.AIOffset[i])*0.98)+self.AIOffset[i]
                self.AIGuess[i] = self.AIList[i].run(input, lastoutput)
            bestscore = max(self.AIScores)
            if bestscore <= 0:
                return 'X'
            
            scoreR = 0
            scoreP = 0
            scoreS = 0
            
            for i in range(0,len(self.AIList)):
                if self.AIScores[i] == bestscore:
                    if self.AIGuess[i] == 'R':
                        scoreR += 100
                    elif self.AIGuess[i] == 'P':
                        scoreP += 100
                    elif self.AIGuess[i] == 'S':
                        scoreS += 100
            
            if scoreR > scoreP and scoreR > scoreS:
                return 'R'
            if scoreP > scoreS and scoreP > scoreR:
                return 'P'
            if scoreS > scoreR and scoreS > scoreP:
                return 'S'
                
            secondbestscore = 0.0
            for i in range(0,len(self.AIList)):
                if self.AIScores[i] != bestscore and self.AIScores[i] > secondbestscore:
                    secondbestscore = self.AIScores[i]
                    
            if secondbestscore <= 0.0:
                return 'X'
                    
            for i in range(0,len(self.AIList)):
                if self.AIScores[i] == secondbestscore:
                    if self.AIGuess[i] == 'R':
                        scoreR += 1
                    elif self.AIGuess[i] == 'P':
                        scoreP += 1
                    elif self.AIGuess[i] == 'S':
                        scoreS += 1
                        
            if scoreR > scoreP and scoreR >= scoreS:
                return 'R'
            if scoreP > scoreS and scoreP >= scoreR:
                return 'P'
            if scoreS > scoreR and scoreS >= scoreP:
                return 'S'
                
            return 'X'
            
        def prune(self, newsize, savefirsttwo):
        
            if savefirsttwo:
                oldAIList = self.AIList[2:]
                self.AIList = [self.AIList[0],self.AIList[1]]
                
                oldAIScores = self.AIScores[2:]
                self.AIScores = [self.AIScores[0],self.AIScores[1]]
                
                oldAIOffset = self.AIOffset[2:]
                self.AIOffset = [self.AIOffset[0],self.AIOffset[1]]
                
                oldAIGuess = self.AIGuess[2:]
                self.AIGuess = [self.AIGuess[0],self.AIGuess[1]]
                
            else:
                oldAIList = self.AIList
                self.AIList = []
                
                oldAIScores = self.AIScores
                self.AIScores = []
                
                oldAIOffset = self.AIOffset
                self.AIOffset = []
                
                oldAIGuess = self.AIGuess
                self.AIGuess = []
            
            numkept = 0
            while numkept < newsize and len(oldAIList) >= 1:
                maxscore = max(oldAIScores)
                i = 0
                while i < len(oldAIList):
                    if oldAIScores[i] == maxscore:
                    
                        self.AIList += [oldAIList[i]]
                        oldAIList = oldAIList[0:i] + oldAIList[i+1:]
                        
                        self.AIScores += [oldAIScores[i]]
                        oldAIScores = oldAIScores[0:i] + oldAIScores[i+1:]
                        
                        self.AIOffset += [oldAIOffset[i]]
                        oldAIOffset = oldAIOffset[0:i] + oldAIOffset[i+1:]
                        
                        self.AIGuess += [oldAIGuess[i]]
                        oldAIGuess = oldAIGuess[0:i] + oldAIGuess[i+1:]
                        
                        numkept += 1
                    
                    i += 1
                        
            
    AI = MetaMerge([(0.0,MetaDoubleRfind(RfindPairs(),Flip(RfindPairs()))), \
                    (0.0,MetaDoubleRfind(RfindInput(),Flip(RfindInput()))), \
                    (-3.0,MetaDoubleRfind(Expectation(),Flip(Expectation()))), \
                    (-10.0,MetaDoubleRfind(ExpectationCut(5),Flip(ExpectationCut(5)))), \
                    (-10.0,MetaDoubleRfind(ExpectationCut(20),Flip(ExpectationCut(20)))), \
                    (-10.0,MetaDoubleRfind(ExpectationCut(50),Flip(ExpectationCut(50)))), \
                    (-10.0,MetaDoubleRfind(ExpectationCut(100),Flip(ExpectationCut(100)))), \
                    (-10.0,MetaDoubleRfind(ExpectationDecay(0.99),Flip(ExpectationDecay(0.99)))), \
                    (-10.0,MetaDoubleRfind(ExpectationDecay(0.95),Flip(ExpectationDecay(0.95)))), \
                    (-10.0,MetaDoubleRfind(ExpectationDecay(0.90),Flip(ExpectationDecay(0.90)))), \
                    (-10.0,MetaDoubleRfind(ExpectationDecay(0.85),Flip(ExpectationDecay(0.85)))), \
                    (-3.0,MetaDoubleRfind(Frequency(),Flip(Frequency()))), \
                    (-10.0,MetaDoubleRfind(FrequencyCut(5),Flip(FrequencyCut(5)))), \
                    (-10.0,MetaDoubleRfind(FrequencyCut(20),Flip(FrequencyCut(20)))), \
                    (-10.0,MetaDoubleRfind(FrequencyCut(50),Flip(FrequencyCut(50)))), \
                    (-10.0,MetaDoubleRfind(FrequencyCut(100),Flip(FrequencyCut(100)))), \
                    (-10.0,MetaDoubleRfind(FrequencyDecay(0.99),Flip(FrequencyDecay(0.99)))), \
                    (-10.0,MetaDoubleRfind(FrequencyDecay(0.95),Flip(FrequencyDecay(0.95)))), \
                    (-10.0,MetaDoubleRfind(FrequencyDecay(0.90),Flip(FrequencyDecay(0.90)))), \
                    (-10.0,MetaDoubleRfind(FrequencyDecay(0.85),Flip(FrequencyDecay(0.85))))])
                    
    output = 'X'
    numrounds = 0
else:
    output = AI.run(input,lastoutput)
    
if output == 'X':
    output = random.choice('RPS')
    
lastoutput = output

numrounds += 1
if numrounds == 50:
    AI.prune(10,True)
if numrounds == 200:
    AI.prune(3,False)