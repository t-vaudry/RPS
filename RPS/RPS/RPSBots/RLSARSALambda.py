# a simple RL agent using SARSA lambda to learn
#


# input is in input, output has to be in output

import random

states = {"R": 0, "P": 1, "S": 2, "start": 3}
actions = ["R", "P", "S"]

rewards = [[0.0, 1.0, -1.0],
           [-1.0, 0.0, 1.0],
           [-1.0, 1.0, 0.0],
           [0.0, 0.0, 0.0]]

def is_undefined(var):
    return not (var in vars() or var in globals())

class RLAgent():
    def __init__(self, states, actions, alpha=0.2, gamma=0.9,
                 epsilon=0.9, lamb=0.9):
        self.states = states
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.lamb = lamb
        self.Q = [ [(1.0/len(actions)) for i in range(len(actions))] for j in
              range(len(states))]
        self.e = [ [(0.0) for i in range(len(actions))] for j in
              range(len(states))]
        self.last_action = 0
        self.last_state = states["start"]
        self.last_reward = 0.0

    def get_action(self, state):
        if random.random() > self.epsilon:
            qs = self.Q[state]
            m = max(qs)
            midx = qs.index(m)
            return midx
        return random.randint(0, len(self.actions) - 1)

    def update_Q(self, state, action, reward):
        Q = self.Q
        e = self.e
        delta = self.last_reward + \
                self.gamma * Q[state][action] - \
                Q[self.last_state][self.last_action]
        e[state][action] += 1 
        for s in range(len(states)):
            for a in range(len(actions)):
                Q[s][a] += self.alpha * delta * e[s][a]
                e[s][a] = self.gamma * self.lamb * e[s][a]
        self.last_reward = reward
        self.last_state = state
        self.last_action = action

def reward(state, action):
    return rewards[state][action]

if is_undefined('rlagent'):
    rlagent = RLAgent(states, actions, 
                      alpha=0.7, gamma=0.7,
                      epsilon=0.9, lamb=0.99)

if input == '':
    input = "start"
state = states[input]

a = rlagent.get_action(state)
r = reward(state, a)
rlagent.update_Q(state, a, r)

output = actions[a]