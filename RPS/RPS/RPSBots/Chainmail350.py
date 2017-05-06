###############################################################################
#                                                                             #
# This is Chainmail350, an RPS program written by PotentProton.               #
#                                                                             #
# This program is a modification on the program I have written named          #
# AmateurSwordsman. It adds a randomized fall-back strategy designed to       #
# guarantee a 35% win rate against even the toughest opponents.               #
#                                                                             #
# For more information on AmateurSwordsman, see                               #
# http://www.rpscontest.com/entry/5679790782676992                            #
#                                                                             #
# The random fall-back strategy uses thresholds which I have precomputed to   #
# be the lowest possible score at any point in time in which a totally random #
# strategy has a 35% chance of a win. This type of strategy is superior to    #
# other forms of defensive random fall-back strategies because of its ability #
# to completely guarantee a certain chance of success. Other strategies that  #
# decide whether to do a random move based on recent performance of           #
# predictors could experience very slow downwards trends without realizing    #
# that in the long run they are losing.                                       #
#                                                                             #
# It is hard to know what is the best threshold to cut off at. Here I have    #
# chosen to guarantee 35% success, but this comes at a cost. There is         #
# inherently some randomness in Rock Paper Scissors, and this program runs a  #
# risk of hitting thresholds at no fault of its own. It is also very hard to  #
# optimize the threshold, as this would require running against the large     #
# number of bad programs that we should be able to beat. I am therefore       #
# submitting multiple versions of this Chainmail program.                     #
#                                                                             #
# The program I used to pre-compute thresholds is included at the end of this #
# file, commented out.                                                        #
#                                                                             #
###############################################################################

import random

if input == "":
	##################################################
	# Create read-only useful conversion structures. #
	##################################################

	# Convert input+output pair to shorthand:
	iop2sh = {'RR':'0','RP':'1','RS':'2','PR':'3','PP':'4','PS':'5','SR':'6','SP':'7','SS':'8'}
	# Get input from shorthand:
	sh2i   = { '0':'R', '1':'R', '2':'R', '3':'P', '4':'P', '5':'P', '6':'S', '7':'S', '8':'S'}
	# Get output from shorthand:
	sh2o   = { '0':'R', '1':'P', '2':'S', '3':'R', '4':'P', '5':'S', '6':'R', '7':'P', '8':'S'}
	
	# Get move that beats given move:
	beat = {'R':'P','P':'S','S':'R'}
	# Get move that loses to given move:
	lose = {'R':'S','P':'R','S':'P'}
	
	####################################
	# Initialize more data structures. #
	####################################
	
	# Move history, for analysis:
	hist = ''
	
	# Current move number:
	now = 0
	
	# Current score:
	score = 0
	
	# Output selections and scores for meta strategies:
	mo = ['X'] * 3
	msc = [0.0] * 3
	
	# Store whether we have switched to a 100% random strategy:
	randstrat = 0
	
	################
	# Select move. #
	################
	
	# Since we have no data to go on, we use randomness.
	output = random.choice(['R','P','S'])
else:
	##################################
	# Check threshold for randomness #
	##################################
	
	# Increment the move number:
	now += 1
	
	# Update the score:
	if input == beat[output]:
		score -= 1
	elif output == beat[input]:
		score += 1
	
	# Switch to a random strategy if we risk not being able to guarantee a 35%
	# chance of a win.
	if score <= -9:
		randstrat = 1
	if now > 88 and score <= -8:
		randstrat = 1
	if now > 270 and score <= -7:
		randstrat = 1
	if now > 431 and score <= -6:
		randstrat = 1
	if now > 573 and score <= -5:
		randstrat = 1
	if now > 694 and score <= -4:
		randstrat = 1
	if now > 795 and score <= -3:
		randstrat = 1
	if now > 876 and score <= -2:
		randstrat = 1
	if now > 937 and score <= -1:
		randstrat = 1
	if now > 977 and score <= 0:
		randstrat = 1
	if now > 997 and score <= 1:
		randstrat = 1
		
	# Output random result if we have switched to randomness, otherwise
	# continue the program as normal.
	if randstrat:
		output = random.choice(['R','P','S'])
	else:
		####################
		# Update raw data. #
		####################
		
		# Record most recent input output pair:
		hist += iop2sh[input+output]
		
		# Update meta strategy scores. We add a decay multiplier of 0.9 to give
		# more weight to more recent events.
		for i in xrange(0,len(mo)):
			# Check that there has actually been a prediction.
			if mo[i] != 'X':
				if mo[i] == beat[input]:
					msc[i] += 1.0
				elif mo[i] == lose[input]:
					msc[i] -= 1.0
				msc[i] *= 0.9
		
		#######################
		# Do pattern matching #
		#######################
		
		# We search for a sequence of events in the history which matches
		# recent events. We try to match longer and longer strings until we
		# fail. The Python rfind function starts at the end of the list and 
		# searches backwards, giving us the most recent occurrence of a
		# sequence. Note that the for loop will not run if now < 2.
		match = -1
		for i in xrange(1,min(15,now-1)):
			localmatch = hist[:(now-1)].rfind(hist[-i:])
			if localmatch != -1:
				# match was found, update with the new best match.
				match = localmatch + i
			else:
				# no reason to continue, next iteration is strictly harder to
				# match.
				break

		if match == -1:
			# No match could be found, so we pick a random output.
			output = random.choice(['R','P','S'])
			# Also reset the meta moves so that we don't rescore moves twice.
			mo = ['X'] * 3
		else:
			# Get shorthand of match from history.
			shmatch = hist[match]
			# Get input/output from shorthand of match.
			imatch = sh2i[shmatch]
		
			###########################################
			# Select output using best meta strategy. #
			###########################################
			
			# Select outputs desired by different strategies.
			mo[0] = imatch
			mo[1] = beat[imatch]
			mo[2] = lose[imatch]
			
			# Find strategy with highest expected value.
			maxmo = 'X' # Output of best meta-strategy.
			maxmsc = -1001 # Score of best meta-strategy.
			maxvalid = 0 # Maximum invalidated in case of conflicting tie.
			for i in xrange(0,len(mo)):
				if msc[i] > maxmsc:
					maxmo = mo[i]
					maxmsc = msc[i]
					maxvalid = 1
				elif (msc[i] == maxmsc) and (mo[i] != maxmo):
					# In the case of a tie between meta strategies, and the
					# meta strategies select different outputs, we should pick
					# a random output instead.
					maxvalid = 0
					
			if maxvalid:
				output = maxmo
			else:
				# Picking random output because of meta strategy tie.
				output = random.choice(['R','P','S'])
				
################################################
# Program used to compute thresholds is below. #
################################################
				
# #!/usr/bin/python
# # usage: findthresholds.py [threshold as fraction of 1.0]

# import sys

# if len(sys.argv) != 2:
	# print "must give exactly one command line argument with your desired threshold"
	# sys.exit(1)

# limit = float(sys.argv[1])
# if limit > 1.0 or limit < 0.0:
	# print "desired threshold should be given as a fraction of 1.0"
	# sys.exit(1)

# bprob = [1.0] * 1000 + [0.0] * 1001
# aprob = [0.0] * 2001

# thresh = [0] * 1000
# for i in reversed(xrange(0,1000)):
	# for j in xrange(0,2001):
		# x = bprob[j-1] if (j != 0) else 1.0
		# y = bprob[j]
		# z = bprob[j+1] if (j != 2000) else 0.0
		# aprob[j] = (x + y + z) / 3.0
		# if aprob[j] > limit:
			# thresh[i] = 1000-(j)
	# tprob = bprob
	# bprob = aprob
	# aprob = tprob

# start = 0
# for i in xrange(1,1000):
	# if thresh[i] != thresh[i-1]:
		# print "Threshold of " + str(thresh[i-1]) + " from " + str(start) + " to " + str(i-1)
		# start = i
# print "Threshold of " + str(thresh[len(thresh)-1]) + " from " + str(start) + " to " + str(len(thresh)-1)