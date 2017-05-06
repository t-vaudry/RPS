import hashlib

s = hashlib.sha256()
if input:
    s.update(input)
output = ['R', 'P', 'S'][sum(map(ord, s.digest())) % 3]