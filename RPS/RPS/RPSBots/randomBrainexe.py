if input:
    _.append(input)
    shuffle(_)
    output=__[_[0]]
else:
    from random import shuffle
    _=[]
    __={"R":"P","P":"S","S":"R"}
    output=__import__("random").choice(["R","P","S"])