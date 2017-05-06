# Rock paper scissors AI

import random


if not input:

	l_move = ['R', 'P', 'S']
	l_historicmoves = []

	# beating dictionary
	d_beat={'R':'P','P':'S','S':'R'}

	# matrix lookup
	d_matrix = {'R': 0, 'P': 1, 'S': 2}

	# index to move dict
	d_matrixinv = {0: 'R', 1: 'P', 2: 'S'}

	output = random.choice(l_move)

else:

	HistoryLen = 50

	# need atleast 100 stored to act
	if len(l_historicmoves) < HistoryLen:
		l_historicmoves.append(input)
		output = random.choice(l_move)
	else:

		# based on what they have played and is stored in our 100 place list. We can predict.
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

		print output