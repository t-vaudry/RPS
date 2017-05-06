if input == "": 
  # Initialization.
  stats = { 
      "R": {"W": 1, "L": 1, "D": 1}, 
      "P": {"W": 1, "L": 1, "D": 1}, 
      "S": {"W": 1, "L": 1, "D": 1}
      }   
  rounds = 0 
else:
  # Update statistics based on previous move.
  stat = stats[output]
  if output == "R":
    if input == "S":
      stat["W"] += 1
    elif input == "P":
      stat["L"] += 1
    else:
      stat["D"] += 1
  elif output == "P":
    if input == "R":
      stat["W"] += 1
    elif input == "S":
      stat["L"] += 1
    else:
      stat["D"] += 1
  elif output == "S":
    if input == "P":
      stat["W"] += 1
    elif input == "R":
      stat["L"] += 1
    else:
      stat["D"] += 1
  rounds += 1

# Play the move that wins most often.
winning_percentage = 0.0 
best_move = ""
for move, stat in stats.iteritems():
  wp = stat["W"] / float(stat["L"] + (stat["D"] * 0.5))
  if wp >= winning_percentage:
    winning_percentage = wp
    best_move = move

output = best_move