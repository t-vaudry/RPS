class ContextTree:
    def __init__(self):
	self.p_kt = 1.0
	self.p = 1.0
	self.counts = [0, 0, 0]
	self.total = 0
	self.children = [None, None, None]
    def update(self, history, i=0):
	x = history[i]
	self.p_kt *= (self.counts[x] + 0.5) / (self.total + 1.5)
	self.total += 1
	self.counts[x] += 1
	if self.total == 1 or i >= min(len(history) - 1, 32):
	    self.p = self.p_kt
            return
	if self.children[x] is None:
	    self.children[x] = ContextTree()
	self.children[x].update(history, i + 1)
	p_children = 1
	for child in self.children:
	    if child is not None:
		p_children *= child.p
	self.p = 0.5 * (self.p_kt + p_children)
    def predict(self, history, i=0):
	x = history[i]
	p_kt = self.p_kt * (self.counts[x] + 0.5) / (self.total + 1.5)
	if self.total == 0 or i >= min(len(history) - 1, 32):
	    return p_kt
	p_children = 1
	for y, child in enumerate(self.children):
	    if child is not None:
		if y == x:
		    p_children *= child.predict(history, i + 1) 
		else:
	            p_children *= child.p
	    elif y == x:
                p_children *= 0.5 / 1.5
	return 0.5 * (p_kt + p_children)

if input == "":
    import collections
    import random
    index = {"R": 0, "P": 1, "S": 2}
    name = ("R", "P", "S")
    beat = (1, 2, 0)
    model = ContextTree()	  
    history = collections.deque([])
    output = random.choice(name)
else:
    i = index[input]
    j = index[output]
    history.appendleft(i)
    history.appendleft(j)
    model.update(history)
    ps = [0.0, 0.0, 0.0]
    for k, _ in enumerate(ps):
	history.appendleft(k)
	ps[k] = model.predict(history)
	history.popleft()
    scores = [0, 0, 0]
    t = sum(ps)
    for _ in xrange(3):
	x = 0
	r = random.uniform(0, t)
	for k, p in enumerate(ps):
	    x += p
	    if  x <= r:
                break
	a = beat[k]
	b = beat[a]
	scores[a] += 1
	scores[b] -= 1
    m = max(scores)
    output = name[random.choice([k for k, x in enumerate(scores) if x == m])]