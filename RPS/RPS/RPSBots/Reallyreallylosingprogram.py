# I bet this won't be the winner.

CHOICES = {
    "R": "P",
    "P": "S",
    "S": "R"
}

if input == "":
    count = {}
    count['R'] = count['P'] = count['S'] = 0
else:
    count[input] += 1

for name, num in count.iteritems():
    if num == max(count.itervalues()):
        mostly_used = name
        break

output = CHOICES[mostly_used]