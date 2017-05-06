#!/usr/bin/env python2
import random

wins = 0
loss = 0

patterns = [["RRR", "P"],
			["PPP", "S"],
			["SSS", "R"]
]

log = ""

def get_throw():
	for pattern in patterns:
		if(pattern[0] == log[-3:]):
			return pattern[1]

	return random.choice("RPS")

output = get_throw()
log += input