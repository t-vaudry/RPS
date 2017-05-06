# Rock paper scissors AI

import random

# In this one I'm going to try and introduce some adaptive behaviour.
# We'll use a few strategies in parallel, say Markov with a few different history sizes and random,
# and we'll switch to the one that has been performing best over the last 100 turns.

# A bit of initialisation.
l_move = ['R', 'P', 'S']

# beating dictionary
d_beat={'R':'P','P':'S','S':'R'}

# losing dictionary
d_lose ={'R':'S','P':'R','S':'P'}

# matrix lookup
d_matrix = {'R': 0, 'P': 1, 'S': 2}

# index to move dict
d_matrixinv = {0: 'R', 1: 'P', 2: 'S'}

performanceWindowSize = 5


# Wrapper class for different strategies.
class Strategy:

        def __init__(self, functionName, predictionLength):
                self.performance = [] # Keep track of performance over the last 100 turns.
                self.name = functionName # This is the function that predicts from previous results.
                self.predictionLength = predictionLength
                self.currentPrediction = 'R'
                self.score = 0 # This score gets updated based on whether the prediction is accurate.

        # How did this prediction method do last turn?
        def CheckLastPrediction(self, actual):
                if len(self.performance) == performanceWindowSize:
                        self.score -= self.performance.pop(0)

                if self.currentPrediction == actual:
                        self.score += 1
                        self.performance.append(1)

                elif self.currentPrediction == d_lose.get(actual):
                        self.score -= 1
                        self.performance.append(-1)

                else:
                        self.performance.append(0)

        def PredictNextTurn(self, history):
                if self.name == "Markov":
                        self.currentPrediction = self.MarkovNextTurn(self.predictionLength, history)
                else:
                        self.currentPrediction = self.RandomNextTurn(self.predictionLength, history)
                        
                return self.currentPrediction

        ################# Prediction functions ####################
        # Markov chain approach
        def MarkovNextTurn(self, predictionLength, history):
                historyLen = len(history)

                if historyLen < predictionLength:
                        return self.RandomNextTurn(0, history)

                # introduce STM 
                STM = [[0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0]]	# each element will initially serve as a counter and then will be percentaged

                l_historicmoves = history[historyLen - predictionLength:]

                for i in range(0, predictionLength - 1):
                        row = d_matrix.get(l_historicmoves[i])			# are we in row R, P or S of our matrix at this index?
                        col = d_matrix.get(l_historicmoves[i + 1])		# which column (column based on next move)
                        
                        STM[row][col] += 1 		# populate counters

                # Note: Not bothering to normalise the rows as no multiplication goes on here!

                # now use the STM to predict the opponents next move

                # simple solution
                # need to know opponents last move, then select highest probability in that moves row and act on it

                MaxProb = max(STM[d_matrix.get(input)]) # Input is global, so this appears to be happy.
                OpponentMoveIndex = 0
                for i, element in enumerate(STM[d_matrix.get(input)]):
                    if MaxProb == element:
                            OpponentMoveIndex = i
                            break

                return d_matrixinv.get(OpponentMoveIndex)
         
        # Random.
        def RandomNextTurn(self, predictionLength, history):
                return random.choice(l_move)

        ############################################################


if not input:

        # Store the history of all moves.
        l_history = []

        # Initialise strategies here.
        strategyIndex = 0

        randomStrategy = Strategy("Random", 0)
        Markov10Strategy = Strategy("Markov", 10)
        Markov50Strategy = Strategy("Markov", 50)
        Markov100Strategy = Strategy("Markov", 100)

        strategies = [randomStrategy, Markov10Strategy, Markov50Strategy, Markov100Strategy]

        # Everyone make a prediction - this will be used for ranking later.
        for strategy in strategies:
                strategy.PredictNextTurn

        # Output the initial prediction (completely random ATM).
	output = strategies[strategyIndex].currentPrediction

else:

        # based on what they have played and is stored in our 100 place list. We can predict.
        # e.g. if list has R -> R 5 times, then convert this into an probability element in the STM

        l_history.append(input)

        # Reassess each strategy.
        for i in range(0, len(strategies)):
                strategies[i].CheckLastPrediction(input)

        # The current strategy should be the one that has been performing best over the last 100.
        bestScore = -1000
        for i in range(0, len(strategies)):
                #print strategies[i].name, " ", strategies[i].score
                if strategies[i].score > bestScore:
                        bestScore = strategies[i].score
                        strategyIndex = i

        print strategyIndex

        # Everyone make a prediction!
        for strategy in strategies:
                strategy.PredictNextTurn(l_history)

        output = d_beat.get(strategies[strategyIndex].currentPrediction)