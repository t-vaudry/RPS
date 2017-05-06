#author: blue-tomato

import random

if input == '':

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
				
	class MetaEnhancedExDecay:

		def __init__(self, child, decay):
			self.child = child
			self.f0 = 0.0
			self.f1 = 0.0
			self.f2 = 0.0
			self.r0prev = 'X'
			self.decay = decay
			
		def run(self, input, lastoutput):
			if input != '':
				if self.r0prev == input:
					self.f1 += 2.0
					self.f2 -= 2.0
				elif self.r0prev == {'R':'P','P':'S','S':'R'}[input]:
					self.f0 += 2.1
					self.f1 -= 2.0
				elif self.r0prev == {'R':'S','P':'R','S':'P'}[input]:
					self.f2 += 2.0
					self.f0 -= 2.0
				
			self.f0 *= self.decay
			self.f1 *= self.decay
			self.f2 *= self.decay
				
			r0 = self.child.run(input, lastoutput)
			self.r0prev = r0
			if r0 == 'X':
				return 'X'
			if self.f0 > self.f1 and self.f0 >= self.f2:
				return r0
			if self.f1 >= self.f0 and self.f1 > self.f2:
				return {'R':'P','P':'S','S':'R'}[r0]
			if self.f2 > self.f0 and self.f2 >= self.f1:
				return {'R':'S','P':'R','S':'P'}[r0]
			if self.f0 == self.f1 and self.f1 == self.f2:
				return 'X'
				
	class Flip:
    
		def __init__(self, child):
			self.child = child
			
		def run(self, input, lastoutput):
			return {'R':'P','P':'S','S':'R','X':'X'}[self.child.run(lastoutput, input)]
			
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
				self.AIScores[i] = ((self.AIScores[i]-self.AIOffset[i])*0.97)+self.AIOffset[i]
				self.AIGuess[i] = self.AIList[i].run(input, lastoutput)
			bestscore = max(self.AIScores)
			
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
				
			secondbestscore = -1000000
			for i in range(0,len(self.AIList)):
				if self.AIScores[i] != bestscore and self.AIScores[i] > secondbestscore:
					secondbestscore = self.AIScores[i]
					
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
			
	AI = MetaMerge([(0.0,MetaEnhancedExDecay(RfindPairs(),0.95)), \
					(-0.5,MetaEnhancedExDecay(Flip(RfindPairs()),0.95))])
			
	output = 'X'
else:
    output = AI.run(input,lastoutput)
    
if output == 'X':
    output = random.choice('RPS')
    
lastoutput = output