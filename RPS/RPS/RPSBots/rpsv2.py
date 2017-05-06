import random

class RockPaperScissors():
    SCORING = {
        'PR':1, 'RS':1, 'SP':1,
        'RR':0, 'SS':0, 'PP':0,
        'RP':-1, 'SR':-1, 'PS':-1
    }
    CONV = {
        'SS':'S', 'PP':'S', 'RR':'S',
        'RP':'U', 'PS':'U', 'SR':'U',
        'PR':'D', 'SP':'D', 'RS':'D'
    }

    def __init__(self):
        self.rounds = 3
        self.wins = 0
        self.ties = 3
        self.losses = 0
        self.opHistRaw = "RPS"
        self.myHistRaw = "RPS"
        self.opHist = "-UU"
        self.myHist = "-UU"
        self.results = [0,0,0]
        self.score = 0.5
        self.recentScore = 0
        self.lookback = 2
        self.last = random.choice(['R', 'P', 'S'])
        self.lastState = None
        self.action = 'U'
        self.actionRaw = 'S'

    def state(self, newState = False):
        n = self.lookback
        s = str(self.results[-n:])+str(self.opHist[-n:])+str(self.myHist[-n:])

        return s

    def play(self, opMove):

        self.rounds += 1
        self.opHistRaw += opMove
        self.opHist += self.CONV[self.opHistRaw[-2:]]
        self.myHistRaw += self.actionRaw
        self.myHist += self.CONV[self.myHistRaw[-2:]]




        self.results += [self.SCORING[self.actionRaw + opMove]]

        self.score = 1.0 * sum(self.results) / self.rounds


## Meet our learning agent, Jack
class Jack:
    def __init__(self, learnRate = 0.01, discountRate = .8, greedy = .005):
        self.learnRate = learnRate  ## how much the Q-values are modified each iteration
        self.discountRate = discountRate  ## how much to discount 'looking ahead'
        self.greedy = greedy  ## how often the agent should make a random choice
        self.updates = 0
        self.q = dict()


    ## Returns initial setting for an entry in the Q table if none exists
    ## Experimenting with different values causes different results
    def InitQValue(self):
        return {'S':0.0, 'U':0.0, 'D':0.0}

    ## Returns what it believes to be the best action based on the Q table,
    ## unless it's one of those greedy (explorative) times
    def MaxQ(self, q):
        #greedy = self.greedy - self.greedy * self.updates / 300000
        ## ^^ experimenting with decreasing chance of exploration over time
        if random.random() < self.greedy or sum(q.values()) == 0.0:
            return random.choice(q.keys())

        best = max(q.values())
        for a in q.keys():
            if q[a] == best:
                action = a
                break

        return action


    ## Given a state, returns an action, based on our action policy
    ## ('Hard-greedy', chooses action corresponding to max Q value almost always)
    def QAction(self, trans=True):
        ss = rps.state()

        if not self.q.has_key(ss):
            self.q[ss] = self.InitQValue()
        a = self.MaxQ(self.q[ss])

        p = rps.myHistRaw[-1]
        go_up = {'R':'P', 'P':'S', 'S':'R'}
        go_down = {'P':'R', 'S':'P', 'R':'S'}
        if a == 'U':
            at = go_up[p]
        elif a == 'D':
            at = go_down[p]
        else:
            at = p

        if trans:
            rps.action = a
            rps.actionRaw = at

            return at
        else:
            return a


    ## This method is the body of the mind, so to speak.
    ## It's called after taking an action and seeing the result, and
    ## the original state, the resulting state, and the action it took
    ## are plugged into the Q algorithm to update the table appropriately.
    def QUpdate(self):
        action = rps.action
        state = rps.lastState
        newState = rps.state()
        result = sum(rps.results[rps.lookback:])

        ss = rps.lastState
        if not self.q.has_key(ss):
            self.q[ss] = self.InitQValue()

        nss = rps.state()
        if not self.q.has_key(nss):
            self.q[nss] = self.InitQValue()

        qValue = self.q[ss][action]
        self.updates += 1

        #self.learnRate = 1.0 / (self.updates / 1000 + 1)
        ## ^^ experimenting with a 1/n style alpha parameter to ensure convergence
        self.q[ss][action] = qValue + self.learnRate * (result +
        #    self.discountRate * max(self.q[nss].values()) - qValue)
        ## ^^ above line is technically the Q algorithm, while the below
        ##    is known as SARSA... but they perform nearly identically
            self.discountRate * self.q[nss][self.QAction(False)] - qValue)

        ## Either way, the learning mechanism is wholely in that one
        ## statement above... i.e.,
        ## Q(s,a) <-- Q(s,a)+alpha(r+lambda*Q(s',t')-Q(s,a))


if input == "":
    rps = RockPaperScissors()
    jack = Jack()


rps.lastState = rps.state()
if input != "":
    rps.play(input)
    jack.QUpdate()
output = jack.QAction()