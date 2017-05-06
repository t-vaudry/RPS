'''
Created on Oct 2, 2012

@author: vinnie

For more information and details about the ELPH sequence predictor, see:
http://vmonaco.com/2012/10/03/dynamic-sequence-prediction-using-entropy-as-a-learning-utility/

The original paper can be found at:
gandalf.psych.umn.edu/users/schrater/Papers/p67-jensen.pdf
'''

import random
from math import log
from itertools import chain
from operator import itemgetter

def xuniqueCombinations(items, n):
    if n==0: yield ()
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield (items[i],)+cc

def powersetNoEmpty(iterable):
    '''
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    '''
    s = list(iterable)
    return chain(*[xuniqueCombinations(s, r) for r in range(1, len(s)+1)])

def reliableEntropy(pspace):
    '''
    Entropy with an additional false positive to remove the bias towards low
    frequency hypothesis
    Returns the reliable entropy
    '''
    total_frequency = sum(pspace.values()) + 1.0
    h_rel = -((1.0/total_frequency) * log(1.0/total_frequency, 2))
    for frequency in pspace.itervalues():
        tmp = frequency/total_frequency
        h_rel -= tmp * log(tmp, 2)
    
    return h_rel

def prune(hspace, h_thresh=1.00):
    '''
    Prune the hypothesis space using the entropy as a threshold
    Returns a pruned hypothesis space
    '''
    for key in hspace.keys():
        if reliableEntropy((key, hspace[key])) > h_thresh:
            hspace.pop(key)
    return hspace

def predict(hspace, stm):
    '''
    Given a short term memory and hypothesis space, make a prediction.
    Returns the prediction, STM item used to make the prediction, and entropy
    '''
    stm_matches = [hspace[p] for p in powersetNoEmpty(stm) if hspace.has_key(p)]
    if len(stm_matches) == 0:
        return None, float('inf')
    
    lowest_entropy = min(stm_matches, key=reliableEntropy)
    h = reliableEntropy(lowest_entropy)
    prediction = max(lowest_entropy.items(), key=itemgetter(1))
    return prediction[0], h

def observe(hspace, stm, observation):
    '''
    Observe and learn a new symbol following the STM.
    Returns the updated hypothesis space.
    '''
    hspace_keys = powersetNoEmpty(stm)
    for key in hspace_keys:
        pspace = hspace.setdefault(key, {})
        pspace.setdefault(observation, 0)
        pspace[observation] += 1
    return hspace

def observeSequence(hspace, sequence, stm_size=7):
    '''
    Observe an entire sequence (not online), and return the hypothesis space.
    '''
    hits = 0
    for i in xrange(stm_size, len(sequence)):
        stm = sequence[i-stm_size:i]
        prediction, h = predict(hspace, stm)
        observe(hspace, stm, sequence[i])
        prune(hspace, 1.0)
        if sequence[i] == prediction:
            print "HIT"
            hits += 1
        else:
            print "MISS"
    print "Correct: ", float(hits)/(len(sequence)-stm_size)
    
    return hspace
    
class OnlineELPH:
    
    def __init__(self, stm_size=7, entropy_thresh=1.0):
        """
        Create on online ELPH sequence predictor
        Really just a wrapper and state holder for the pure functions above
        """
        self.hspace = {}
        self.stm = []
        self.stm_size = stm_size
        self.entropy_thresh = entropy_thresh
        return
    
    def observe(self, next_mem, observation):
        """
        Observe a symbol.
        Also updates the STM and prunes the hypothesis space
        """
        observe(self.hspace, self.stm, observation)
        self.stm.append(next_mem)
        if len(self.stm) > self.stm_size:
            self.stm = self.stm[-self.stm_size:]
        return
    
    def predict(self):
        """
        Make a prediction
        """
        return predict(self.hspace, self.stm)
    
if input == '':
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    output = random.choice(['R','P','S'])
    elph = OnlineELPH(stm_size=3, entropy_thresh=1.5)
    feedback_elph = OnlineELPH(stm_size=3, entropy_thresh=1.5)
else:
    elph.observe(input, input)
    p1, h1 = elph.predict()
    p2, h2 = feedback_elph.predict()
    
    if h1 < h2:
        prediction = p1
    else:
        prediction = p2
        
    if prediction and random.random() > 0.3:
        output = beat[prediction]
    else:
        output = output = random.choice(['R','P','S'])
        
    feedback_elph.observe(output, input)