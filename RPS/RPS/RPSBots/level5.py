import random

beat = {"R": "P", "P": "S", "S": "R"}
rps = ["R", "P", "S"]    

if input == "":
  seq_in = ["R", "P", "S"]
  seq_out = ["R", "P", "S"]
  output = random.choice(["R", "P", "S"])
  seq_out.append(output)

  couples = [[[[i+j+k+l for l in rps] for k in rps] for j in rps] for i in rps]
  couples = [c for i in couples for j in i for k in j for c in k]

  predictors = dict(zip(couples, [[0, 0, 0] for k in couples]))
else:
  seq_in.append(input)
  if len(seq_in) < 3:
    output = random.choice(["R", "P", "S"])
    seq_out.append(output)
  else:
    predictors[seq_out[-3]+seq_in[-3]+seq_out[-2]+seq_in[-2]][rps.index(input)] += 1

    move_predictor = predictors[seq_out[-2]+seq_in[-2]+seq_out[-1]+input]
    best_prediction = rps[move_predictor.index(max(move_predictor))]

    output = beat[best_prediction]

    seq_out.append(output)