import random

beat = {'R':'P', 'P':'S', 'S':'R', '':''}


output = random.choice(["R","P","S"])

if input == "":
	h = ""
        d = 0
        lastOut = ""
else:
	h += input
        if beat[lastOut] == input:
                d -= 1
        elif beat[input] == lastOut:
                d += 1

        if -15 <= d <= 10 and len(h) >= 20:
                if len(h) <= 100 and h[-7:] in ['RRRRRRR', 'PPPPPPP', 'SSSSSSS']:
			output = beat[h[-1]]
		elif len(h) <= 300 and h[-8:] in ['RRRRRRRR', 'PPPPPPPP', 'SSSSSSSS']:
			output = beat[h[-1]]
		elif h[-3:] == h[-6:-3] == h[-9:-6]:
			output = random.choice([beat[h[-3]], h[-3]])
		elif len(h) <= 50 and h[-4:] in ['RRRR', 'PPPP', 'SSSS']:
			output = h[-1]
		elif len(h) <= 150 and h[-5:] in ['RRRRR', 'PPPPP', 'SSSSS']:
			output = h[-1]
		elif h[-6:] in ['RRRRRR', 'PPPPPP', 'SSSSSS']:
			output = h[-1]
		elif h[-3:] == h[-6:-3] == h[-9:-6]:
			output = beat[h[-3]]
lastOut = output