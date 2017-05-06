# I bet this won't we the winner :-)

CHOICES = {
    "R": "S",
    "P": "R",
    "S": "P"
}

if input == "":
    count = {}
    count['R'] = count['P'] = count['S'] = 0
else:
    count[input] += 1

mostly_used = max(count)
output = CHOICES[mostly_used]