if input == "": # initialize variables for the first round
	rockCount=paperCount=scissorsCount=0
	RR=RP=RS=PR=PP=PS=SR=SP=SS=0
	prev=""
elif input == "R":
	if prev=="R": RR+=1
	elif prev=="P": RP+=1
	elif prev=="S": RS+=1
	prev="R"
elif input == "P":
	if prev=="R": PR+=1
	elif prev=="P": PP+=1
	elif prev=="S": PS+=1
	prev="P"
elif input == "S":
	if prev=="R": SR+=1
	elif prev=="P": SP+=1
	elif prev=="S": SS+=1
	prev="S"
if prev=="R":
	rockCount=RR
	paperCount=PR
	scissorsCount=SR
elif prev=="P":
	rockCount=RP
	paperCount=PP
	scissorsCount=SP
elif prev=="S":
	rockCount=RS
	paperCount=PS
	scissorsCount=SS
	
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors