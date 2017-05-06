import itertools
import re
from random import randint


global HTH, rounds, AIwins, humanWins, draws, choiceArr, threeCharCount
HTH = ""
rounds = 0
AIwins = 0
humanWins = 0
draws = 0
choiceArr = ["R","P","S"]
threeCharCount = [0,0,0]


#for finding indices where substrings begin
def find_substring(substring, string):
    """
    Returns list of indices where substring begins in string

    find_substring('me', "The cat says meow, meow")
    [13, 19]
    """
    indices = []
    index = -1  # Begin at -1 so index + 1 is 0
    while True:
        # Find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:
            break  # All occurrences have been found
        indices.append(index)
    return indices

#finds largest indices in list
def maxelements(seq):
    ''' Return list of position(s) of largest element '''
    max_indices = []
    if seq:
        max_val = seq[0]
        for i,val in ((i,val) for i,val in enumerate(seq) if val >= max_val):
            if val == max_val:
                max_indices.append(i)
            else:
                max_val = val
                max_indices = [i]

    return max_indices

#gets the AI throw, based on several factors
def getAIThrow():
    #first: get last three characters of HTH and pattern match it
    lastChars = HTH[-3:]
    tpIndices = find_substring(lastChars, HTH)
    threeCharCount = [0,0,0]
    for sIndex in tpIndices:
        nextIndex = sIndex + 3;
        if nextIndex < (len(HTH)):
            if HTH[nextIndex] == 'R':
                threeCharCount[0]+=1
            if HTH[nextIndex] == 'P':
                threeCharCount[1]+=1
            if HTH[nextIndex] == 'S':
                threeCharCount[2]+=1
    #find largest index of three char count and choose it as next throw
    #if tie, choose from them at random

    mostThrownThree = maxelements(threeCharCount)
    mttLen = len(mostThrownThree)

    if mttLen == 1:
        choice = choiceArr[mostThrownThree[0]]
        if choice == "R":
            return "P"
        if choice == "S":
            return "R"
        if choice == "P":
            return "S"

    if mttLen == 2:
        preChoice = randint(0,1)
        choice = choiceArr[preChoice]
        if choice == "R":
            return "P"
        if choice == "S":
            return "R"
        if choice == "P":
            return "S"

    if mttLen == 3:
        preChoice = randint(0,2)
        choice = choiceArr[preChoice]
        if choice == "R":
            return "P"
        if choice == "S":
            return "R"
        if choice == "P":
            return "S"

if input == '':
    output = choiceArr[randint(0,2)]

else:
    if len(HTH) <= 5:
        output = choiceArr[randint(0,2)]
        HTH+=input

    else:
        HTH+=input
        AIThrow = getAIThrow()
        output = AIThrow