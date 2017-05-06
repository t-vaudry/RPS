if input == "":
    import random
    import math

    class NN(object):

        learnrate = {"RS": 0.01, "SP": 0.01, "PR": 0.01,
                     "RR": 0.2, "SS": 0.2, "PP": 0.2,
                     "SR": 0.5, "PS": 0.5, "RP": 0.5}
        
        def __init__(self, num_moves):
            self.num_moves = num_moves
            #number of nodes
            self.ni = 6 * self.num_moves
            self.no = 3
            #init activations
            self.ia = [0] * self.ni
            self.oa = [0] * self.no
            #init weights
            #initial weights need to be below 3/self.ni
            self.weights = dict([((i, j), 0)
                                 for i in range(self.ni)
                                 for j in range(self.no)])
         
        def feed(self, moves):        
            self.ia = moves_to_repr(moves[-2 * self.num_moves:])
            self.oa = [sum(self.weights[(i, j)] * self.ia[i]
                           for i in range(self.ni))
                       for j in range(self.no)]
            return self.oa

        def train(self, moves):
            #hebb learning rule
            target_repr = moves_to_repr(win[moves[-1]])
            learnrate = self.learnrate[moves[-2:]]
            error = map(lambda x, y: x - y, target_repr, self.oa)
            for i in range(self.ni):
                for j in range(self.no):
                    self.weights[(i, j)] += (learnrate * error[j] * self.ia[i] /
                                             self.ni * 3)

    def moves_to_repr(moves):
        nninput = []
        for c in moves:
            nninput += repr_lookup[c]
        return nninput

    def repr_to_move(nnoutput):
        index = max(enumerate(nnoutput), key=lambda x:x[1])[0]
        return ciphers[index]


    ciphers = "RSP"
    win = dict(zip("RSP", "PRS"))
    repr_lookup = {"R": [1, 0, 0], "S": [0, 1, 0], "P" : [0, 0, 1]}

    nn = NN(5)
    moves = "R" * 10
    ourmove = nn.feed(moves)
    output = repr_to_move(ourmove)
    moves += output
else:
    moves += input
    nn.train(moves)
    ourmove = nn.feed(moves)
    output = repr_to_move(ourmove)
    moves += output