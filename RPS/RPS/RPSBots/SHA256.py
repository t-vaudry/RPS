from hashlib import sha256

state = ''

throws = ['R', 'P', 'S']

if input:
    state = state + input

output = throws[int(sha256(state).hexdigest(), 16) % len(throws)]