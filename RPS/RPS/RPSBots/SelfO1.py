#By David Catt (2013)
#Take its own output as a context
if input == "":
    TOVAL = {"R":0,"P":1,"S":2}
    TOCHR = ["P","S","R"]
    last = 0
    count = [[1] * 3] * 3
else:
    count[last][TOVAL[input]] += 1
if count[last][0] > count[last][1]:
    if count[last][2] > count[last][0]:
        last = 2
    else:
        last = 0
else:
    if count[last][2] > count[last][1]:
        last = 2
    else:
        last = 1
output = TOCHR[last]