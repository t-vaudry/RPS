import collections

counts = collections.defaultdict(int)

def common():
  ret = ""
  c = 0
  for key, count in counts.iteritems():
    if count > c:
      ret = key
      c = count
  return ret

if input == "":
  output = "S"
else:
  counts[input] += 1
  most_common = common()
  if most_common == "R":
    output = "P"
  if most_common == "P":
    output = "S"
  if most_common == "S":
    output = "R"