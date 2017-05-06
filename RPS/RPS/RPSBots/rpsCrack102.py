import random
SIZE = 5
WEIGHT_FACTOR = 6.

class HistoryNode(object):
    def __init__(self, parent=None):
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        self.children = {'RR': None, 'RS': None, 'RP': None, 'SR': None, 'SS': None,
                         'SP': None, 'PR': None, 'PS': None, 'PP': None}

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
            self.distribution[last_move] = self.distribution[last_move] * 0.975 + 1

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

        for i in xrange(2, len(self.input) + 1, 2):
            self.root.new_move(self.input[-i:])

    def predict(self):
        results = {'R':0, 'S':0, 'P':0}
        for i in xrange(2, len(self.input) + 1, 2):
            res = self.root.predict(self.input[-i:])
            #print res
            if res is not None:
                for key in res:
                    results[key[1]] += res[key] * (WEIGHT_FACTOR ** i)

        d = results
        e = d.keys()
        e.sort(cmp=lambda a, b: cmp(d[a], d[b]))
        return e[-1]


if input == '':
    history_tree_me = HistoryTree()
    history_tree_him = HistoryTree()
    output = random.choice(["R", "P", "S"])
    pred = {'R':'P', 'S':'R', 'P':'S'}
    meta_predictor = [output] * 6
    metascore = [0] * 6
    counter = 0
    win = ['RS', 'SP', 'PR']
    lost = ['SR', 'PS', 'RP']
    possible_moves = ['R', 'P', 'S']
else:
    history_tree_me.new_move(output + input)
    history_tree_him.new_move(input + output)
    counter += 1
        
    for idx in xrange(len(metascore)):
        if meta_predictor[idx] + input in win:
            metascore[idx] = metascore[idx] * 0.9 + 1
        elif meta_predictor[idx] + input in lost:
            metascore[idx] = metascore[idx] * 0.9 - 1
        else:
            metascore[idx] = metascore[idx] * 0.9 - 0.34
            
        
    prediction_me = history_tree_me.predict()
    prediction_him = history_tree_him.predict()
    for i in range(3):
        move_me = possible_moves[(possible_moves.index(prediction_me) + i) % 3]
        move_him = possible_moves[(possible_moves.index(prediction_him) + i) % 3]
        meta_predictor[i] = move_me
        meta_predictor[i + 3] = move_him
    
    best_predictor = metascore.index(max(metascore))

    play_random = True
    for score in metascore:
        if score > 2:
            play_random = False
    #very simple switching / adapting strategie        
    if play_random:
        output = random.choice(["R", "P", "S"])
    else:
        output = meta_predictor[best_predictor]