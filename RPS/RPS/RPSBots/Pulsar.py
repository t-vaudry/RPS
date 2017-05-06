# pulsar
# by cjfaure

# so basically it uses fibonacci numbers
# to continually switch between strategies.

# like the other one, this one's more of an
# experiment to see how strategies would
# react. It's not really meant to win.

import random

try:
	if rh <= fib[1]:
		fib = [fib[1], sum(fib)]
		strat = (strat + 1) % len(strat_lambdas)
	enbg /= 3
	enbg += "RPS".index(input)
except: # yup, it's the first round
	fib = [0, 1]
	rh = 0
	strat_lambdas = [
		lambda i: i+1,
		lambda i: i+2,
		lambda i: 3-i,
		lambda i: 2-i
	]
	strat = 0
	enbg = 0
output = "PRSPR"[strat_lambdas[strat](int(enbg))]
if int(fib[0]+rh)%2: output = "RPS"["SRP".index(output)]
rh += random.random()*3