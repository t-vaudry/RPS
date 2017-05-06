import random

#Simple program to test system release 3

if (input == ""):
    rCount = 0;
    sCount = 0;  
    pCount = 0;

if (input == "R"):
    rCount = rCount + 1;
elif (input == "S"):
    sCount = sCount + 1;
elif (input == "P"):
    pCount = pCount + 1;

if ((rCount >= sCount) and (rCount >= pCount)):
    output = "P";
elif ((sCount >= rCount) and (sCount >= pCount)):
    output = "R";
elif ((pCount >= rCount) and (pCount >= sCount)):
    output = "S";