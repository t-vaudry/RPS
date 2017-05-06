import random
# ORDER HERE MATTERS! going X-1 will be a winning direction
options=["S","P","R"]

def beat(input):
  return options[options.index(input)-1]


def who_won(them,me):
  if them==me:
    return 0
  if beat(them)==me:
    return 1
  return -1


def establish_score(decision_matrix,step,turns_back=1):
  if step!=1:
    choice_tree=establish_score(decision_matrix,step-1,turns_back+1)
  else:
    choice_tree=[]
    # So, ["RP","PR"]
  them = input_log[-1*turns_back]
  me = output_log[-1*turns_back]
  choice_tree.insert(0,them+me)
  leaf = decision_matrix
  for step in choice_tree:
    branch = leaf
    if step in leaf:
      leaf = leaf[step]
    else:
      leaf[step] = {
        "value": 0,
      }
      leaf = leaf[step]
    score_at_leaf = who_won(them,me) * 1.0
    old_value = leaf["value"] / turns_back
    leaf["value"]=score_at_leaf + old_value
  return choice_tree


def locate_current_choices(turns_back):
  if turns_back!=1:
    choice_tree=locate_current_choices(turns_back-1)
  else:
    choice_tree=[]
    # So, ["RP","PR"]
  them = input_log[-1*turns_back]
  me = output_log[-1*turns_back]
  choice_tree.append(them+me)
  return choice_tree


def find_choice(choice_tree):
  leaf = decision_matrix
  for step in choice_tree:
    branch = leaf
  decision_weights = {"R":0,"P":0,"S":0}
  for their_choice in options:
    for my_choice in options:
      step = their_choice+my_choice
      if step in branch:
        decision_weights[my_choice] = decision_weights[my_choice] + branch[step]["value"]
      else:
        # Cycle backwards through, game theory
        decision_weights[my_choice] = decision_weights[my_choice] + who_won(my_choice,their_choice) / 3.0

  c_output = "R"
  c_output_val = decision_weights[c_output]
  for i in decision_weights:
    if decision_weights[i] > c_output_val:
      c_output_val = decision_weights[i]
      c_output = i
    if decision_weights[i] == c_output_val:
      c_output = random.choice([i,c_output,i]) # It's better to change your mind
    if decision_weights[i] == 0:
      c_output = i # Fill out the decision tree

  return c_output


# Main script code starts here
if input not in options:
  # Game beginning
  input_log = []
  output_log = []
  decision_matrix = {}
else:
  input_log.append(input)

if input not in options:
  # Pick a random starting position
  output = random.choice(options)
else:
  # Store last turn's values
  who_won_last = who_won(input,output_log[-1])

  # Here is where the magic happens
  d_weight = {"R":0,"P":0,"S":0}

  establish_score(decision_matrix,min(3,len(input_log)),1)
  
  avoid_sames = False
  # In case we're facing opposition that likes to pick the same thing, defend against it
  cases={}
  for i in input_log[-3:]:
    cases[i] = 1
  if len(cases) == 1:
    # The last three choices they made were the same
    dont_pick = input_log[-1]
    if len(input_log) > 3:
      if input_log[-4] == input_log[-3]:
        # They seem to be on a chain, choose the victor over that choice, expecting the same from them
        output = beat(dont_pick)
        avoid_sames = random.choice([True,False,True])

  if not avoid_sames:
    output = find_choice(locate_current_choices(min(2,len(input_log))))

output_log.append(output)