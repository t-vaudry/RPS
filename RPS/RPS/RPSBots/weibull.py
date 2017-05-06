import random

B = ["R","P","S"]
o = random.weibullvariate(5.2,3.14)
output = B[int(o)%3]