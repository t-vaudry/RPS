import random
import collections

rounds = 2

class SimpleMarkovTransitionTable:
    memory = []

    def remember(self, i):
        self.memory.append(i)

    def play(self):
        if (len(self.memory) > 2):
            max = 0
            index = 0
            table = [[0 for _ in range(3)] for _ in range(3)]
            for (x, y), c in collections.Counter(zip(self.memory, self.memory[1:])).items():
                table[x][y] = c

            for i in range(0, 3, 1):
                sum = table[i][0] + table[i][1] + table[i][2]
                for j in range(0, 3, 1):
                    table[i][j] /= sum
            for j in range(0, 3, 1):
                if table[0][j] > max:
                    index = j
                    max = table[0][j]

            if index == 0:
                return "P"
            elif index == 1:
                return "S"
            elif index == 2:
                return "R"
        else:
            return random.choice(["R","P","S"])

m = SimpleMarkovTransitionTable()
m.remember(input)
output = m.play()