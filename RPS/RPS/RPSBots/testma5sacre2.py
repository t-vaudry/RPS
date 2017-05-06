#was interested in a detail

from hashlib import sha256


state = 'e+4sk6jfPPON3muIQJPM-KBCJPyYHgkkgXgpprL2'
output = 'RPS'[int(sha256(state).hexdigest(),16)%3]