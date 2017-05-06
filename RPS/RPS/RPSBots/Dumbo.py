if not input:
	count1 = count2 = count3 = 0
else:
	if input == lastMove:
		offset += 1
	if (input=="R" and lastMove=="S") or (input=="P" and lastMove=="R") or (input=="S" and lastMove=="P"):
		offset += 2
	offset = offset%3
	if offset == 0:
		count1 += 1
	elif offset == 1:
		count2 += 1
	else:
		count3 += 1
if (count1 > count2) and (count1 > count3):
	offset = 0
	output = input
elif (count2 > count3):
	offset = 1
	if input=="R":
		output = "P"
	elif input=="P":
		output = "S"
	else:
		output = "R"
else:
	offset = 2
	if input=="R":
		output = "S"
	elif input=="P":
		output = "R"
	else:
		output = "P"
lastMove = output