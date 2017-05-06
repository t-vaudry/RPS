import random

beat = {"R": "P", "P": "S", "S": "R"}
rps = ["R", "P", "S"]    

if input == "":
  seq_in = ["R", "P", "S"]
  seq_out = ["R", "P", "S"]
  output = random.choice(["R", "P", "S"])
  seq_out.append(output)

  couples = ["RR", "RP", "RS", "PR", "PP", "PS", "SR", "SP", "SS"]
  predictors = dict(zip(couples, [[0, 0, 0] for k in couples]))
else:
  seq_in.append(input)
  if len(seq_in) < 2:
    output = random.choice(["R", "P", "S"])
    seq_out.append(output)
  else:
    predictors[seq_out[-2]+seq_in[-2]][rps.index(input)] += 1

    move_predictor = predictors[seq_out[-1]+input]
    best_prediction = rps[move_predictor.index(max(move_predictor))]

    output = beat[best_prediction]

    seq_out.append(output)