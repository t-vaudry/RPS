#!/usr/bin/env python2
# $File: prob.py
# $Date: Sat May 03 14:04:28 2014 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>


if input == '':
    from collections import defaultdict
    import random

    # let O denote opponent, S denote self

    # (O_1, M_1, O_2) -> count
    cnt_oppo = defaultdict(int)

    # (O_1, M_1, M_2) -> count
    cnt_self = defaultdict(int)

    last_oppo = None
    last_self = None

    # history of all moves
    history = ''


    beat = dict(R='P', P='S', S='R')

    def play(s):
        global output, history, last_self, cnt_self
        if not (last_self is None):
            cnt_self[last_self + last_oppo + s] += 1
        last_self = output = s
        history += s

    def get_prob_O2(O, MO):
        return cnt_oppo[MO + O]

    def get_prob_M2(M, MO):
        return cnt_self[MO + M]

    def get_prob_O4(O, MOMO):
        return get_prob_O2(O, MOMO[:2]) * get_prob_O2(MOMO[1], MOMO[2:]) * \
                get_prob_M2(MOMO[0], MOMO[2:])

    def get_prob_M4(O, MOMO):
        return get_prob_M2(O, MOMO[:2]) * get_prob_M2(MOMO[1], MOMO[2:]) * \
                get_prob_O2(MOMO[0], MOMO[2:])

    def get_max_idx(vec):
        m = max(vec)
        idx = [i for i in range(3) if vec[i] == m]
        return random.choice(idx)

    def result(me, other):
        global beat
        if me == other:
            return 0
        if me == beat[other]:
            return 1
        return -1

    def log(s):
        pass
        # with open('/tmp/test', 'a') as fout:
        #    print >> fout, str(s)

    def make_move():
        global history

        # P(O_3 | M_1 O_1 M_2 O_2)
        if len(history) >= 4:
            oppo = map(lambda s: get_prob_O4(s, history[-4:]), 'RPS')
            self = map(lambda s: get_prob_M4(s, history[-4:]), 'RPS')
            ps = []
            for i in range(3):
                p = 0.0
                me = self[i]
                for j in range(3):
                    other = oppo[j]
                    p += result('RPS'[i], 'RPS'[j]) * other
                ps.append(p)
            # log(ps)
            # log(get_max_idx(ps))

            return 'RPS'[get_max_idx(ps)]

        return random.choice('RPS')

else:
    if last_oppo != None and last_self != None:
        cnt_oppo[last_self + last_oppo + input] += 1
    history += input

    last_oppo = input

play(make_move())
# vim: foldmethod=marker