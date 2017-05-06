# searching for a past pattern and using it to predict the opponent's next move

import math
import random

# returns the hand that beats this hand
def beats(hand):
   if hand == 'R':
      return 'P'
   elif hand == 'P':
      return 'S'
   else:
      return 'R'

def randHand():
   hands = ['R', 'P', 'S']
   random.shuffle(hands)
   return hands[0]

def randWeightedHand(ps):
   r = random.random()
   if r < ps['R']:
      return 'R'
   elif r < ps['R'] + ps['P']:
      return 'P'
   else:
      return 'S'

# finds the length of the match from searchIndex and matchIndex leftward
def searchPatternLengthBackwards(lst, searchIndex, matchIndex, indexLimit, lengthLimit):
   length = 0
   while searchIndex >= indexLimit and matchIndex >= indexLimit and \
      length < lengthLimit and lst[searchIndex] == lst[matchIndex]:
      searchIndex -= 1
      matchIndex -= 1
      length += 1
   return length

# calculates the weight of a pattern match based on length and distance
# the distance is from the index where the match is found to the current playing index
def weighPattern(length, lengthLimit, distance, distanceLimit):
   if length > 0:
      lengthWeight = length * length
      distanceWeight = ((distanceLimit - distance) / float(distanceLimit)) + 1
      return lengthWeight * distanceWeight
   else:
      return 0

# calculates the weights of the opponent's next move
def calculateWeights(lst, index, distanceLimit, lengthLimit):
   indexLimit = index - distanceLimit
   weights = {'R':0.0, 'P':0.0, 'S':0.0}
   for i in xrange(index - 1, indexLimit - 1, -1):
      length = searchPatternLengthBackwards(lst, i, index, indexLimit, lengthLimit)
      distance = index - i
      weight = weighPattern(length, lengthLimit, distance, distanceLimit)
      if weight > 0:
         weights[lst[i+1]] += weight
   return weights

# uses the calculated weights to make a prediction about the opponent's next hand
def predict(lst, index, distanceLimit, lengthLimit, cutoffWeight):
   weights = calculateWeights(lst, index, distanceLimit, lengthLimit)
   sum = weights['R'] + weights['P'] + weights['S']
   if sum < cutoffWeight:
      return randHand()
   else:
      weights['R'] /= sum
      weights['P'] /= sum
      weights['S'] /= sum
      return randWeightedHand(weights)

# some global variables to keep track of history and stuff
hands = []
lastHand = None
handsPlayed = 0

# start of main code
if input == '':
   output = randHand()
   lastHand = output
   handsPlayed += 1
else:
   hands.append(input)
   hands.append(lastHand)
   
   distanceLimit = int(math.sqrt(handsPlayed))
   lengthLimit = distanceLimit
   
   prediction = predict(hands, handsPlayed - 1, lengthLimit, distanceLimit, 0.5)
   output = beats(prediction)
   
   lastHand = output
   handsPlayed += 1