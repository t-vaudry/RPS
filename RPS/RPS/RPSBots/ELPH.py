import random, math

def observe(symbol):
    updateHypothesisSpace(symbol)
    pruneHypothesisSpace()
    shortTermMemory.append(symbol)
    if len(shortTermMemory) > shortTermMemorySize:
        del shortTermMemory[0]
        
def updateHypothesisSpace(symbol):
    shortTermMemoryPowerset = powerset(shortTermMemory)
    for context in shortTermMemoryPowerset:
        tcontext = tuple(context)
        if tcontext in longTermMemory.keys():
            if symbol in longTermMemory[tcontext]:
                longTermMemory[tcontext][symbol] += 1
            else:
                longTermMemory[tcontext][symbol] = 1
        else:
            longTermMemory[tcontext] = {}
            longTermMemory[tcontext][symbol] = 1
            
def pruneHypothesisSpace():
    remove = [context for context in longTermMemory.keys() if normalisedShannonEntropy(longTermMemory[context]) > hypothesisShannonEntropyThreshold]
    for context in remove: del longTermMemory[context]
            
def getMostLikely(contexts):
    minRseDistributions = []
    minRse = float("inf")
    for context in contexts:
        tcontext = tuple(context)
        if tcontext in longTermMemory.keys():
            rse = reliableNormalisedShannonEntropy(longTermMemory[tcontext])
            if rse < minRse:
                minRse = rse;
                minRseDistributions = []
                minRseDistributions.append(longTermMemory[tcontext])
            elif rse == minRse:
                minRseDistributions.append(longTermMemory[tcontext])
    if minRseDistributions:
        return random.choice(minRseDistributions)
    else:
        return None
    
def predict():
    return getMostLikely(powerset(shortTermMemory))
                
    
# def powerset(iterable):
#     s = list(iterable)
#     return itertools.chain().from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def powerset(seq): 
    if len(seq) <= 1: 
        yield seq 
        yield [] 
    else: 
        for item in powerset(seq[1:]): 
            yield [seq[0]]+item 
            yield item

def normalisedShannonEntropy(distribution):
    se = 0
    s = sum(distribution.values())
    for v in distribution.values():
        t = v / s
        if len(distribution) != 1:
            if t > 0:
                n = math.log(t)
                d = math.log(len(distribution))
                t2 = t * (n / d)
                if not math.isnan(t2):
                    se += t2
    return -se

def reliableNormalisedShannonEntropy(distribution):
    rse = 0
    s = sum(distribution.values())
    for v in distribution.values():
        t = v / (s + 1)
        if len(distribution) != 1:
            if t > 0:
                n = math.log(t)
                d = math.log(len(distribution))
                t2 = t * (n / d)
                if not math.isnan(t2):
                    rse += t2
    t = 1 / (s + 1)
    if len(distribution) != 1:
        if t > 0:
            n = math.log(t)
            d = math.log(len(distribution))
            rse += t * (n / d)
    return -rse

if input == "":
    shortTermMemory = []
    shortTermMemorySize = 4
    longTermMemory = {}
    hypothesisShannonEntropyThreshold = 0.999
    output = random.choice(['R', 'P', 'S'])
else:
    observe(input)
    prediction = predict()
    if prediction:
        maxSymbol = max(prediction, key=prediction.get)
        if maxSymbol == 'R':
            output = 'P'
        elif maxSymbol == 'P':
            output = 'S'
        elif maxSymbol == 'S':
            output = 'R'
        else:
            output = random.choice(['R', 'P', 'S'])
    else:
        output = random.choice(['R', 'P', 'S'])