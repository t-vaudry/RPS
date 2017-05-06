scoring = {
    "R": {
        "R": 0,
        "P": -1,
        "S": 1
    },
    "P": {
        "R": 1,
        "P": 0,
        "S": -1
    },
    "S": {
        "R": -1,
        "P": 1,
        "S": 0
    }
}
output = "S"
if input:
  for k,v in scoring[input].iteritems() :
    if v == 1:
      output = k