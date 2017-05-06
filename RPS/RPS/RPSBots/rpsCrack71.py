import random
SIZE = 10
WEIGHT_FACTOR = 4.5

class HistoryNode(object):
    def __init__(self, parent=None):
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        self.children = {'RR': None, 'RS': None, 'RP': None, 'SR': None, 'SS': None, 'SP': None,
                         'PR': None, 'PS': None, 'PP': None}

        self.distribution = {'RR': 0, 'RS': 0, 'RP': 0, 'SR': 0, 'SS': 0, 'SP': 0,
                             'PR': 0, 'PS': 0, 'PP': 0}

    def new_move(self, input):
        #analyse last move
        last_move = input[0:2]

        if len(input) > 2:
            if self.children[last_move] is None:
                self.children[last_move] = HistoryNode(self)
            self.children[last_move].new_move(input[2:])
        else:
            if last_move in wins:
                self.distribution[last_move] += 0.7
            elif last_move in loose:
                self.distribution[last_move] -= 0.8
                self.distribution[conter[last_move]] += 0.5
            else:
                self.distribution[last_move] -= 0.1
                self.distribution[conter[last_move]] += 0.5

    def predict(self, input):
        if len(input) > 0:
            last_move = input[0:2]
            if self.children[last_move] is not None:
                return self.children[last_move].predict(input[2:])
            else:
                return None
        else:
            return self.distribution


class HistoryTree(object):
    def __init__(self):
        self.root = HistoryNode()

        self.input = ''

    def new_move(self, move):
        self.input += move
        if len(self.input) > SIZE * 2:
            self.input = self.input[-SIZE * 2:]

        for i in xrange(2,len(self.input)+1,2):
            self.root.new_move(self.input[-i:])

    def predict(self):
        results = {'R':0, 'S':0, 'P':0}
        for i in xrange(2, len(self.input)+1, 2):
            res = self.root.predict(self.input[-i:])
            #print res
            if res is not None:
                for key in res:
                    results[key[1]] += res[key] * (WEIGHT_FACTOR**i)

        d = results
        e = d.keys()
        e.sort(cmp=lambda a,b: cmp(d[a],d[b]))
        return e[-1]


if input == '':
    history_tree = HistoryTree()
    output = random.choice(["R","P","S"])
    pred = {'R':'P','S':'R','P':'S'}
    wins = ['PR', 'RS', 'SP']
    draw = ['PP', 'RR', 'SS']
    loose = ['RP', 'SR', 'PS']
    conter = {'RR': 'PR', 'RP': 'SP', 'SS': 'RS', 'PS': 'RS', 'PP': 'SP', 'SR':'PR'}
else:
    history_tree.new_move(output + input)
    prediction = history_tree.predict()
    output = pred[prediction]