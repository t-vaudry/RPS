def most_common(l):
    max = 0
    maxitem = None
    for x in set(l):
        count =  l.count(x)
        if count > max:
            max = count
            maxitem = x
    return maxitem

if input == "": # initialize variables for the first round
        history=''
        history += 'R'


history += input

output=most_common(history)