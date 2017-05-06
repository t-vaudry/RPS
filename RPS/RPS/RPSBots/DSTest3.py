import random

maxListSize = 4
output = random.choice(["R","P","S"])
  
if input == "":
  rockList = []
  paperList = []
  scissorList = []
  
elif input == "R":
  rock = rockList.count("R")
  paper = rockList.count("P")
  scissor = rockList.count("S")
  
  if rock > paper and rock > scissor:
    output = "P"
  elif paper > scissor:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rockList.append(input)
    if len(rockList) > maxListSize:
      rockList.pop(0)
  elif last == "P":
    paperList.append(input)
    if len(paperList) > maxListSize:
      paperList.pop(0)
  elif last == "S":
    scissorList.append(input)
    if len(scissorList) > maxListSize:
      scissorList.pop(0)
  
elif input == "P":
  rock = paperList.count("R")
  paper = paperList.count("P")
  scissor = paperList.count("S")
  
  if rock > paper and rock > scissor:
    output = "P"
  elif paper > scissor:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rockList.append(input)
    if len(rockList) > maxListSize:
      rockList.pop(0)
  elif last == "P":
    paperList.append(input)
    if len(paperList) > maxListSize:
      paperList.pop(0)
  elif last == "S":
    scissorList.append(input)
    if len(scissorList) > maxListSize:
      scissorList.pop(0)
  
elif input == "S":
  rock = scissorList.count("R")
  paper = scissorList.count("P")
  scissor = scissorList.count("S")
  
  if rock > paper and rock > scissor:
    output = "P"
  elif paper > scissor:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rockList.append(input)
    if len(rockList) > maxListSize:
      rockList.pop(0)
  elif last == "P":
    paperList.append(input)
    if len(paperList) > maxListSize:
      paperList.pop(0)
  elif last == "S":
    scissorList.append(input)
    if len(scissorList) > maxListSize:
      scissorList.pop(0)
  
last = input