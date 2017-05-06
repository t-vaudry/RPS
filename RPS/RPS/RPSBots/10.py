KAMEN, SKARJE, PAPIR = 0, 1, 2

class Player:

    def __init__(self):
        self.name = "Jure Slak"
        self.history = "";
        self.count = [1, 1, 1]

    def play(self):
        return self.w_choice(zip([PAPIR,KAMEN,SKARJE],map(lambda x: float(x)/sum(self.count), self.count)))

    def other(self, sign):
        assert 0 <= sign <= 2
        self.history += str(sign);
        self.count[sign] += 1

    def __str__(self):
        return ""+\
               "Player Jure Slak\
"+\
               "History: {0}\
".format(self.history[len(self.history)-50:])+\
               "Count: K: {1}   S: {2}    P{3}\
".format(*self.count)

    def __repr__(self): return str(self)

    def w_choice(self, lst):
        import random
        n = random.uniform(0, 1)
        for item, weight in lst:
                if n < weight: break
                n -= weight
        return item

p = Player()

invleg = {'R': KAMEN, "S": SKARJE, "P": PAPIR}

if input:
    p.other(invleg[input])

output = "RSP"[p.play()]