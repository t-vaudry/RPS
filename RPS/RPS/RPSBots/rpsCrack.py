"""
A data structure to remeber the last moves of rsp.
"""
import random

class HistoryNode(object):
    def __init__(self, parent=None):
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        self.children = {'R': None, 'S': None, 'P': None}

        self.distribution = {'R':0, 'S':0, 'P':0}

    def new_move(self, input):
        #analyse last move
        last_move = input[0]

        if len(input) > 1:
            if self.children[last_move] is None:
                self.children[last_move] = HistoryNode(self)
            self.children[last_move].new_move(input[1:])
        else:
            self.distribution[last_move] += 1

    def predict(self, input):
        if len(input) > 0:
            last_move = input[0]
            if self.children[last_move] is not None:
                return self.children[last_move].predict(input[1:])
            else:
                return None
        else:
            return self.distribution


class HistoryTree(object):
    def __init__(self):
        self.root = HistoryNode()

        self.input = ''

    def new_move(self, input):
        self.input += input
        if len(self.input) > 10:
            self.input = self.input[-10:]

        for i in xrange(1,len(self.input)+1):
            self.root.new_move(self.input[-i:])

    def predict(self):
        results = {'R':0,'S':0,'P':0}
        for i in xrange(1, len(self.input)+1):
            res = self.root.predict(self.input[-i:])
            #print res
            if res is not None:
                for key in res:
                    results[key] += res[key] * (1.5**i)

        d = results
        e = d.keys()
        e.sort(cmp=lambda a,b: cmp(d[a],d[b]))
        return e[-1]


if input == '':
    history_tree = HistoryTree()
    output = random.choice(["R","P","S"])
    pred = {'R':'P','S':'R','P':'S'}
else:
    history_tree.new_move(input)
    prediction = history_tree.predict()
    output = pred[prediction]