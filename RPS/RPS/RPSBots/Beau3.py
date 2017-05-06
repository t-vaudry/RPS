# Rock paper scissors AI

# In this version I would like to introduce a way to resize the history window
# dynamically to improve performance - Alex

import random

if not input:

	l_move = ['R', 'P', 'S']

        l_allhistoricmoves = []
	l_historicmoves = []

	# beating dictionary
	d_beat={'R':'P','P':'S','S':'R'}

	# matrix lookup
	d_matrix = {'R': 0, 'P': 1, 'S': 2}

	# index to move dict
	d_matrixinv = {0: 'R', 1: 'P', 2: 'S'}

        HistoryLen = 50  # Default value.
        timeSinceLastWindowChange = 0
        timeInEachWindow = 1  # How frequently it changes window. It seems 1 works best - makes it very hard to predict.

	output = random.choice(l_move)

else:
        l_allhistoricmoves.append(input)

	# need atleast 100 stored to act
	if len(l_historicmoves) < HistoryLen:
		l_historicmoves.append(input)
		output = random.choice(l_move)
	else:
                timeSinceLastWindowChange += 1
                tooShort = False

                # Is it time to change window size?
                if timeSinceLastWindowChange == timeInEachWindow:
                        HistoryLen = random.randint(10, 100)
                        timeSinceLastWindowChange = 0

                        # If the historicmoves list is too long then truncate it...
                        lenDiff = len(l_historicmoves) - HistoryLen
                        if lenDiff > 0:
                                del l_historicmoves[:lenDiff]
                        elif lenDiff < 0: # Need more data for this window!
                                output = random.choice(l_move)
                                tooShort = True

                if not tooShort:
                        # based on what they have played and is stored in our history list. We can predict.
                        # e.g. if list has R -> R 5 times, then convert this into an probability element in the STM

                        l_historicmoves.pop(0)				# will only have 100 to analyse at one time
                        l_historicmoves.append(input)

                        # introduce STM 
                        STM = [[0.0,0.0,0.0], [0.0,0.0,0.0], [0.0,0.0,0.0]]	# each element will initially serve as a counter and then will be percentaged

                        for i in range(0, HistoryLen - 1):
                                row = d_matrix.get(l_historicmoves[i])			# are we in row R, P or S of our matrix at this index?
                                col = d_matrix.get(l_historicmoves[i + 1])		# which column (column based on next move)
                                
                                STM[row][col] += 1 		# populate counters

                        # normalise (each row adds up to one)
                        for i in range(0, 3):
                                rowsum = sum(STM[i])	 # sum up elements of this row 

                                if rowsum == 0:				# special case 
                                        STM[i][i] = 1
                                        continue

                                for j in range(0, 3):		
                                        STM[i][j] /= rowsum		# directly divide each element of the matrix 


                        # now use the STM to predict the opponents next move

                        # simple solution
                        # need to know opponents last move, then select highest probability in that moves row and act on it

                        MaxProb = max(STM[d_matrix.get(input)])
                        OpponentMoveIndex = 0
                        for i, element in enumerate(STM[d_matrix.get(input)]):
                                if MaxProb == element:
                                        OpponentMoveIndex = i
                                        break

                        OppenentsMove = d_matrixinv.get(OpponentMoveIndex)



                        output = d_beat.get(OppenentsMove)