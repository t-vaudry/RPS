'''
This program attempts to emulate the New York Times RPS program.
It can be found at:
https://www.nytimes.com/interactive/science/rock-paper-scissors.html
'''
def searchPast(history,l):
    if l < 1:
        return "S"
    if l >= len(history):
        return searchPast(history,l-1)
    last = []
    last.extend(history[len(history)-l:])
    match = []
    i = 0
    while i < len(history)-l:
        if history[i:i+l] == last:
            match.append(history[i+l])
        i += 1
    if match == []:
        return searchPast(history,l-1)
    maxi = ("P", match.count("R"))
    if match.count("P") > maxi[1]:
        maxi = ("S", match.count("P"))
    if match.count("S") > maxi[1]:
        maxi = ("R", match.count("S"))
    return maxi[0]
if input:
    history.append(input)   
else:
    history = []
output = searchPast(history,5)