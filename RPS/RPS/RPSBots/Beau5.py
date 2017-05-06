# Rock paper scissors AI
# This bot is named after my dog: "Beau". May he live long and prosper.

# In this version I introduce an additional prediction method: greedy pattern matching.
# I may also implement some meta-strategies.

# The "meta-prediction" is the move that would beat the move that the opponent would play to beat the prediction. Obviously.
# I'm going to maintain one of these for each strategy.

import random

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

# Are we currently using the meta-strategy?
meta = False


# Wrapper class for different strategies.
class Strategy:

        def __init__(self, functionName, predictionLength):
                self.performance = [] # Keep track of performance over the last so many turns.
                self.metaperformance = [] 
                self.name = functionName # This is the function that predicts from previous results.
                self.predictionLength = predictionLength
                self.currentPrediction = 'R'
                self.metaPrediction = 'S'
                self.score = 0 # This score gets updated based on whether the prediction is accurate.
                self.metascore = 0

        # How did this prediction method do last turn?
        def CheckLastPrediction(self, actual):
                if len(self.performance) == performanceWindowSize:
                        self.score -= self.performance.pop(0)
                        self.metascore -= self.metaperformance.pop(0)

                # Deal with normal prediction.
                if self.currentPrediction == actual:
                        self.score += 1
                        self.performance.append(1)

                elif self.currentPrediction == d_lose.get(actual):
                        self.score -= 1
                        self.performance.append(-1)

                else:
                        self.performance.append(0)

                # Deal with meta-prediction.
                if self.metaPrediction == actual:
                        self.metascore += 1
                        self.metaperformance.append(1)

                elif self.metaPrediction == d_lose.get(actual):
                        self.metascore -= 1
                        self.metaperformance.append(-1)

                else:
                        self.metaperformance.append(0)


        def PredictNextTurn(self, history):
                if self.name == "Markov":
                        self.currentPrediction = self.MarkovNextTurn(self.predictionLength, history)
                elif self.name == "GreedyPattern":
                        self.currentPrediction = self.GreedyPatternMatchNextTurn(self.predictionLength, history)
                else:
                        self.currentPrediction = self.RandomNextTurn()
                        
                # Update the "meta-prediction".
                self.metaPrediction = d_beat.get(self.currentPrediction)

                if meta:
                        return self.metaPrediction
                else:
                        return self.currentPrediction

        ################# Prediction functions ####################
        # Markov chain approach
        def MarkovNextTurn(self, predictionLength, history):
                historyLen = len(history)

                if historyLen < predictionLength:
                        return self.RandomNextTurn()

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

        def GreedyPatternMatchNextTurn(self, predictionLength, history):
                # This predictor looks at the history and tries to find the most similar looking pattern 
                # to the one that has just happened. It is greedy mas it always tries to match as many turns
                # as possible. Once the most similar pattern is found - we play the counter for the move that
                # was played next.
                # Note: The predictionLength is used if we want to cap how far back it can search.
                
                # Convert list to string so we can search more easily.
                shistory = ''.join(turn for turn in history) # Total history.

                # Restrict history.
                if predictionLength != 0:
                        shistory = shistory[len(shistory) - predictionLength:]

                historylen = len(shistory)
                shistory_trunc = shistory[:historylen - 1] # Every element but the last - obviously the current pattern occurred at the end!

                mostCharactersFound = 0
                currentSearchAmount = 1 # How many we are trying to match.
                bestIndex = -1
                currentIndex = shistory_trunc.rfind(shistory[historylen - currentSearchAmount:]) 
                while currentIndex != -1 and historylen - 1 - currentSearchAmount > -1:
                        mostCharactersFound = currentSearchAmount
                        bestIndex = currentIndex
                        currentSearchAmount += 1
                        currentIndex = shistory_trunc.rfind(shistory[historylen - currentSearchAmount:]) 

                # OK, how have we done...
                if bestIndex == -1: # Never found any matches...
                        return self.RandomNextTurn()
                else:
                        return shistory[bestIndex + mostCharactersFound] # The character after the best pattern.
                        
        # Random.
        def RandomNextTurn(self):
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
        GreedyPattern10Strategy = Strategy("GreedyPattern", 10)
        GreedyPattern50Strategy = Strategy("GreedyPattern", 50)
        GreedyPattern100Strategy = Strategy("GreedyPattern", 100)
        GreedyPatternStrategy = Strategy("GreedyPattern", 0)

        strategies = [randomStrategy, Markov10Strategy, Markov50Strategy, GreedyPattern10Strategy, GreedyPattern50Strategy, GreedyPattern100Strategy]

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
                if strategies[i].score > bestScore:
                        meta = False
                        bestScore = strategies[i].score
                        strategyIndex = i

                if strategies[i].metascore > bestScore:
                        meta = True 
                        bestScore = strategies[i].metascore
                        strategyIndex = i

        #print strategyIndex, meta

        # Everyone make a prediction!
        for strategy in strategies:
                strategy.PredictNextTurn(l_history)

        output = d_beat.get(strategies[strategyIndex].currentPrediction)