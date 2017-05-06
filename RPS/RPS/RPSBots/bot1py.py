if not input:
	ngrams = []

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
		if(len(ngrams) > len(content)):
			ngram = [g for g in ngrams[len(content)-1] if g.content == content] #find match

			if ngram:
				return ngram[0]

	def add(content):
		if len(content) > 10:
			return
			
		for i in range(len(ngrams), len(content)):
			ngrams.append([]) #append until len(ngrams) == len(content)

		ngram = find_match(content)

		if ngram: 	#if match found
			ngram.count += 1
		else: 		#else
			ngram = NGram(content=content, length=len(content))
			ngrams[len(content)-1].append(ngram)

	def recent_content():
		return ngrams[len(ngrams)-1][0].content[:]

	def add_new(content):
		rc = recent_content()
		for i in range(0, len(rc)):
			add(rc[i:] + content)

	def best_move():
		rc = recent_content()

		R = 0
		P = 0
		S = 0

		rcR = rc + 'R'
		rcP = rc + 'P'
		rcS = rc + 'S'
		
		for i in range(1, len(rcR)):
			ngram = find_match(rcR[i:])

			if ngram:
				R += ngram.length * ngram.count

		for i in range(1, len(rcP)):
			ngram = find_match(rcP[i:])

			if ngram:
				P += ngram.length * ngram.count

		for i in range(1, len(rcS)):
			ngram = find_match(rcS[i:])

			if ngram:
				S += ngram.length * ngram.count

		if S > R and S > P:
			return 'R'
		elif P > R and P > S:
			return 'S'
		else:
			return 'P'
	
	output = 'R'

else:
	if len(ngrams) > 0:
		add_new(input)
	add(input)

	output = best_move()