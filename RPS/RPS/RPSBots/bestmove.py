if input == "": 
  # Initialization.
  stats = { 
      "R": {"W": 0, "L": 0, "D": 0}, 
      "P": {"W": 0, "L": 0, "D": 0}, 
      "S": {"W": 0, "L": 0, "D": 0}
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
max_wins = 0 
best_move = ""
for move, stat in stats.iteritems():
  if stat["W"] >= max_wins:
    max_wins = stat["W"]
    best_move = move

output = best_move