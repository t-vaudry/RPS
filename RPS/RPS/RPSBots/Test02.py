import random

#Simple program to test system release 2

if (input == ""):
   rCount = 0;
   sCount = 0;  
   pCount = 0;
   tCount = 0;

if (input == "R"):
   rCount = rCount + 1;
elif (input == "S"):
   sCount = sCount + 1;
elif (input == "P"):
   pCount = pCount + 1;

tCount = (rCount + sCount + pCount) + 1;

pOut = rCount/tCount;
rOut = sCount/tCount;
sOut = pCount/tCount;

if ((pOut >= rOut) and (pOut >= sOut)):
   output = "P";
elif ((rOut >= pOut) and (rOut >= sOut)):
   output = "R";
elif ((sOut >= pOut) and (sOut >= rOut)):
   output = "S";