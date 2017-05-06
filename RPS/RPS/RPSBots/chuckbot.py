from collections import defaultdict
from heapq import nlargest
from operator import itemgetter
import random

class Counter(dict):
	def __init__(self, iterable=[], **kwds):
		self.update(iterable, **kwds)

	def __missing__(self, key):
		return 0

	def most_common(self, n=None):
		if n is None:
			return sorted(self.iteritems(), key=itemgetter(1), reverse=True)
		return nlargest(n, self.iteritems(), key=itemgetter(1))

	def update(self, iterable=None, **kwds):
		if iterable is not None:
			if hasattr(iterable, 'iteritems'):
				if self:
					self_get = self.get
					for elem, count in iterable.iteritems():
						self[elem] = self_get(elem, 0) + count
				else:
					dict.update(self, iterable) # fast path when counter is empty
			else:
				self_get = self.get
				for elem in iterable:
					self[elem] = self_get(elem, 0) + 1
		if kwds:
			self.update(kwds)

def buildMC(history, op_history, order):
	n = len(history)
	mc = defaultdict(Counter)
	for i in xrange(order, n-1):
		tup = tuple(history[i-order:i])
		mc[tup].update((op_history[i],))
	return mc


if input == '':
	history = []
	op_history = []
	hist_maxlen = 100
	order = 2
else:
	op_history.append(input)

if len(history) > hist_maxlen:
	remove = hist_maxlen-len(history)
	history = history[remove:]
	op_history = op_history[remove:]

if len(history) >= hist_maxlen:
	mc = buildMC(history, op_history, order)
	output, freq = mc[tuple(history[-order:])].most_common(1)[0]
else:
	output = random.choice(["R","P","S"])


history.append(output)