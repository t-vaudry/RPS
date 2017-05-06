if input:
    his.append(input)
    __import__("random").shuffle(his)
    output=_[his[0]]
else:
    _={"R":"P","P":"S","S":"R"}
    his = []
    output = "R"