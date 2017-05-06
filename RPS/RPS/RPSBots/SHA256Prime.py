from hashlib import sha256

throws = ['R', 'P', 'S']
beat_throw = { 'R' : 'P', 'P' : 'S', 'S' : 'R' }

# This claim isn't true for SHA256-Prime :-(
if input == '':
    state = 'I win against bots that always throw the same thing!'
else:
    state = state + output

sha256_output = throws[int(sha256(state).hexdigest(), 16) % len(throws)]

# Output throw that beats SHA256
output = beat_throw[sha256_output]