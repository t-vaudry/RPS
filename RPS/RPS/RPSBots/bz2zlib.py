# uses built-in python modules for compression as a predictor
import bz2
import zlib
import random
if not input:
    s = ''
    output = random.choice('RPS')
else:
    s += input
    zxcv = [len(bz2.compress(s+x,9)) + len(zlib.compress(s+x,9)) for x in 'RPS']
    output = 'PSR'[zxcv.index(min(zxcv))]