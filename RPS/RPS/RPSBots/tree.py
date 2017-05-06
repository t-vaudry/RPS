class Node:
  def __init__(self):
    self.scores = {"R":0,"P":0,"S":0}
    self.children = {}

  def add_move(self, move):
    self.scores[move[0]] += 1
    if move in self.children:
      child = self.children[move]
    else:
      child = Node()
      self.children[move] = child
    return child, child.scores

  def __str__(self):
    return("scores: R={0} P={1} S={2}".format(self.scores["R"], self.scores["P"], self.scores["S"]))




class Node_Ptr:
  def __init__(self, node):
    self.node = node


if not input:
  root = Node()
  node_ptrs = [Node_Ptr(root)]
  DECAY = .8
  BEATS = {"R":"P","P":"S","S":"R"}
  output = "R"
else:
  move = input + output
  scores = {"R":0,"P":0,"S":0}
  for node_ptr in node_ptrs:
    node = node_ptr.node
    node, new_scores = node.add_move(move)
    scores = dict((x, (scores.get(x,0) + new_scores.get(x,0)) * DECAY) for x in scores.keys())
    node_ptr.node = node
  node_ptrs.append(Node_Ptr(root))
  if len(node_ptrs) > 10:
    del node_ptrs[0]
  output = BEATS[max(scores, key=scores.get)]