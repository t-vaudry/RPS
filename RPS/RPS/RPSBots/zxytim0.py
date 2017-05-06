# Rock-Paper-Scissors

import random
# rock 0
# paper 1
# Scissors 2
# results: -1 lose, 0 draw, 1 win

class Agent(object):

    def play(self):
        pass

    def feedback(self, o):
        pass


class RandomAgent(Agent):
    def play(self):
        return random.randint(0, 2)

    def feedback(self, s):
        pass


def get_result(me, oppo):
    if me == oppo:
        return 0
    if me == (oppo + 1) % 3:
        return 1
    return -1


class StrategicAgent(Agent):

    def __init__(self, choice):
        self.last = -1
        self.history = []
        self.oppo_history = []
        self.results = []
        self.choice = choice

    def _do_play(self, s):
        self.history.append(s)
        self.last = s
        return s

    def play(self):
        if self.last == -1:
            return self._do_play(random.randint(0, 2))
        if random.random() < 0.01:
            return self._do_play(random.randint(0, 2))
        if self.results[-1] == 1:  # win
            if self.choice == 0:
                # change strategy
                options = filter(lambda x: x != self.last, range(3))
                return self._do_play(random.choice(options))
            else:
                # play what opponent last plays
                return self._do_play(self.oppo_history[-1])

        else:  # lose
            # play what could beat the opponent
            return self._do_play((self.oppo_history[-1] + 1) % 3)

    def feedback(self, o):
        self.oppo_history.append(o)
        self.results.append(get_result(self.last, o))


class Arena(object):

    def run(self, agent_0, agent_1, nr_times):
        rst = [0, 0, 0]

        for i in range(nr_times):
            s0 = agent_0.play()
            s1 = agent_1.play()
            agent_0.feedback(s1)
            agent_1.feedback(s0)
            rst[get_result(s0, s1) + 1] += 1

        return rst

char2num = dict(R=0, P=1, S=2)   
num2char = "RPS"                 
                                 
if input == "":                  
    agent = StrategicAgent(0)    
else:                            
    s = char2num[input]          
    agent.feedback(s)            
                                 
output = num2char[agent.play()]