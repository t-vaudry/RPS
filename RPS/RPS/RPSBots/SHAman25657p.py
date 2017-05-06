from hashlib import sha256

# The constant used here came to me in a dream.
state = input and state + input or 'e+4sk5jfPPON3muIQJPM-KBCJPyYHgkkgXgpprL2'
output = 'RPS'[int(sha256(state).hexdigest(),16)%3]