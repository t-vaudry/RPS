import random

def sublistExists(list, sublist):
    for i in range(len(list)-len(sublist)+1):
        if sublist == list[i:i+len(sublist)]:
            return i
    return -1

class History:

    MAX_HISTORY_SIZE = 100

    opponentMoves = []

    def save(self, opponentMove):
        self.opponentMoves.append(opponentMove)

        if len(self.opponentMoves) > self.MAX_HISTORY_SIZE:
            self.opponentMoves = self.opponentMoves[self.MAX_HISTORY_SIZE:]

    def selectPattern(self, patternLength):
        pattern = self.opponentMoves[-patternLength:]
        return pattern

    def selectSearchSpace(self, spaceLength):
        return self.opponentMoves[:spaceLength]

    def predictOpponentsNextMove(self):
        patternLength = int(round(len(self.opponentMoves)/2, 0)) + 1
        patternIndex = -1

        while patternIndex == -1 and patternLength > 1:
            patternLength -= 1
            pattern = self.selectPattern(patternLength)
            searchSpace = self.selectSearchSpace(len(self.opponentMoves) - patternLength)
            patternIndex = sublistExists(searchSpace, pattern)

        if patternIndex >= 0:
            nextMoveIndex = patternIndex + patternLength
            return self.opponentMoves[nextMoveIndex]
        else:
            return random.choice(["R", "P", "S"])

if input == "": # initialize variables for the first round
    history = History()
    beat={'R':'P','P':'S','S':'R'}
    output = random.choice(["R","P","S"])
else:
    history.save(input)
    output = beat[history.predictOpponentsNextMove()]