def prob(dist):
    tot = dist[0] + dist[1] + dist[2]
    if tot == 0:
        return 0.5
    else:
        return (dist[2] + (dist[1] / 2.0)) / tot
    
if input == "":
    #constants
    RPSVAL = {"R":0,"P":1,"S":2}
    RPSCHR = ["R","P","S"]
    OUTCOME = [[1,0,2],[2,1,0],[0,2,1]]
    #self
    sord = 1
    smask = 3**sord
    sctx = 0
    #opponent
    oord = 1
    omask = 3**oord
    octx = 0
    #stats
    stats = [[[[0.0] * 3] * 3] * omask] * smask
    last = 0
else:
    stats[sctx][octx][last][OUTCOME[last][RPSVAL[input]]] += 1.0
    sctx = ((sctx * 3) + last) % smask
    octx = ((octx * 3) + RPSVAL[input]) % omask
tmp = stats[sctx][octx]
pr = prob(tmp[0])
pp = prob(tmp[1])
ps = prob(tmp[2])
if pr > pp:
    if ps > pr:
        last = 2
    else:
        last = 0
else:
    if ps > pp:
        last = 2
    else:
        last = 1
output = RPSCHR[last]