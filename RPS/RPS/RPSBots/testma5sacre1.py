#I'm just testing. Please ignore.

from hashlib import sha256


state = input and state + input or 'e+4sk6jfPPON3muIQJPM-KBCJPyYHgkkgXgpprL2'
output = 'RPS'[int(sha256(state).hexdigest(),16)%3]