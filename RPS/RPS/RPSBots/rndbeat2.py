import random

counter = {'R': 'P', 'P': 'S', 'S': 'R'}

if input == "":
  opp_played = []
  opp_played_dict = {'R': [], 'P':[], 'S':[]}
  mylastmove = None
  output = random.choice(['R', 'P', 'S'])
else:
  opp_played.append(input)
  if mylastmove:
    opp_played_dict[mylastmove].append(input)

  if mylastmove is None:
    output = random.choice(['R', 'P', 'S'])
  elif opp_played_dict[mylastmove] == []:
    expected = random.choice(opp_played)
    output = counter[expected]
  else:
    expected = random.choice(opp_played_dict[mylastmove])
    output = counter[expected]

mylastmove = output