if input == "":
  round = 1
else:
  round += 1

if round < 51:
  output = "R"
elif round == 51:
  output = "S"
elif (output == "R" and input == "P") or (output == "P" and input == "S") or (output == "S" and input == "R"):
  output = input