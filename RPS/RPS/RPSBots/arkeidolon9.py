if not input:
	import random

	ngrams = []
	LIMIT = 10000

	rc = ""

	class NGram:
		content = ""
		length = 0
		count = 1

		def __init__(self, content, length):
			self.content = content
			self.length = length

		def __repr__(self):
			return str([self.content, self.count])

	def find_match(content):
		length = len(content)

		if(len(ngrams) >= length):
			ngram = [g for g in ngrams[length-1] if g.content == content] #find match

			if ngram:
				return ngram[0]

	def add(content):
		length = len(content)
		for i in range(len(ngrams), length):
			ngrams.append([]) #append until len(ngrams) == len(content)

		ngram = find_match(content)

		if ngram: 	#if match found
			ngram.count += 1
		else: 		#else
			ngram = NGram(content, length)
			ngrams[length-1].append(ngram)

	def add_new(content):
		length = len(rc)

		for i in range(max(0, length-LIMIT), length):
			add(rc[i:] + content)

	def best_move():
		R = P = S = 0
		length = len(rc)

		for i in range(max(0, length-LIMIT), length):
			ngram = find_match(rc[i:]+'R')

			if ngram:
				R += ngram.count ** ngram.length

		for i in range(max(0, length-LIMIT), length):
			ngram = find_match(rc[i:]+'P')

			if ngram:
				P += ngram.count ** ngram.length

		for i in range(max(0, length-LIMIT), length):
			ngram = find_match(rc[i:]+'S')

			if ngram:
				S += ngram.count ** ngram.length

		best = max(R, P, S)
		choices = []

		if R == best:
			choices.append('P')
		if P == best:
			choices.append('S')
		if S == best:
			choices.append('R')

		return random.choice(choices)
	
	output = random.choice(['R', 'P', 'S'])

else:
	add_new(input)
	add(input)

	rc += input
	rc = rc[LIMIT:]

	output = best_move()