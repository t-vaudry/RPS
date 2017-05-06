if input == "": # initialize variables for the first round
	count = rockCount = paperCount = scissorsCount = 0;
	
elif input == "R":
	rockCount += 1;
elif input == "P":
	paperCount += 1;
elif input == "S":
	scissorsCount += 1;
	
count += 1;

if rockCount == 0 and scissorsCount == 0 and paperCount == 0:
	output = "R" # go rock the first time because rock rules!
elif rockCount == 0 and scissorsCount == 0:
	output = "S";
elif rockCount == 0 and paperCount == 0:
	output = "R";
elif scissorsCount == 0 and paperCount == 0:
	output = "P";
else:

	rPercent = rockCount / count;
	pPercent = paperCount / count;
	sPercent = scissorsCount / count;

	# assume they go with what they have rolled the least
	if rPercent < pPercent and rPercent < sPercent:
		output = "P";
	elif pPercent < rPercent and pPercent < sPercent:
		output = "S";
	else:
		output = "R"; # rock is our core, always go home with rock