# searching for a past pattern and using it to predict the opponent's next move
# seems like only matching opponent's hands is better than trying to match opponents and own hands
# also only consider patterns after which the opponent wins or ties, since the opponent is more likely to play those hands

import math
import random

# the hand that beats this hand
beats = {'R':'P', 'P':'S', 'S':'R'}

def randHand():
   return random.choice(['R', 'P', 'S'])

def win(mine, other):
   return mine == beats[other]

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
      temp = length * length
      temp2 = temp * temp
      lengthWeight = temp2
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
      # count it only if after that pattern was a tie or a loss
      if not win(my_hands[i+1], lst[i+1]):
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

# start of main code
if input == '':
   hands_played = []
   my_hands = []
   hands = 1
   
   output = randHand()
   lastHand = output
else:
   hands_played.append(input)
   my_hands.append(lastHand)
   
   distanceLimit = min(hands - 1, 100)
   lengthLimit = min(hands - 1, 30)
   
   prediction = predict(hands_played, hands - 1, lengthLimit, distanceLimit, 0.5)
   output = beats[prediction]
   
   lastHand = output
   hands += 1