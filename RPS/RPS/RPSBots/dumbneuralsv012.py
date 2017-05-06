#trying with higher learn rates compared to dumbneurals-v0.1

if input == "":
    import random
    import math

    class NN(object):
        #high leranrates spoil counter strategy bots
        #but might diminish ability to learn simple strategy bots
        #TODO change learn rates dynamically depending on recent performance
        learnrate = {"win": 0.2, "tie": 0.9, "loss": 0.9}
        
        def __init__(self, ins):
            #number of nodes
            self.ni = ins
            self.no = 3
            #init activations
            self.ia = [0] * self.ni
            self.oa = [0] * self.no
            #init weights
            #initial weights need to be below 3/self.ni
            self.weights = [[random.uniform(0, 3./self.ni) for i in range(self.ni)]
                            for j in range(self.no)]
         
        def feed(self, inps):        
            self.ia = inps
            self.oa = [sum(self.weights[j][i] * self.ia[i]
                           for i in range(self.ni))
                       for j in range(self.no)]
            return self.oa

        def train(self, target, result_last_round):
            #hebb learning rule
            #factor of 1/self.ni*3 is there to ensure output
            #in range 0,1 if lernrates are < 1
            #and inputs are 1 for every third inputnode
            #maybe important for convergence
            learnrate = self.learnrate[result_last_round]
            error = map(lambda x, y: x - y, target, self.oa)
            for i in range(self.ni):
                for j in range(self.no):
                    self.weights[j][i] += (learnrate * error[j] * self.ia[i] /
                                             self.ni * 3)

    def moves_to_repr(moves):
        nninput = []
        for c in moves:
            nninput += repr_lookup[c]
        return nninput

    def repr_to_move(nnoutput):
        ciphers = "RSP"
        index = max(enumerate(nnoutput), key=lambda x:x[1])[0]
        return ciphers[index]


    repr_lookup = {"R": [1, 0, 0], "S": [0, 1, 0], "P" : [0, 0, 1]}
    result = {"RS": "win", "SP": "win", "PR": "win",
              "RR": "tie", "SS": "tie", "PP": "tie",
              "SR": "loss", "PS": "loss", "RP": "loss"}
    num_moves = 5 #number of recent rounds the neurons get to see
    nn = NN(num_moves * 6)
    history = "RP" * num_moves
    
    def feedneurons():
        inps = moves_to_repr(history[-2 * num_moves:])
        ourmove = nn.feed(inps)
        return repr_to_move(ourmove)

    def trainneurons():
        win = dict(zip("RSP", "PRS"))
        target = moves_to_repr(win[history[-1]])
        last_round = history[-2:]
        nn.train(target, result[last_round])
        
    
    output = feedneurons()
    history += output
else:
    history += input
    trainneurons()
    output = feedneurons()
    history += output