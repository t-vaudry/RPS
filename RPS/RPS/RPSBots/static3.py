if input == "":
    plays = ['R','R','R','S','S','S','P','P','P']	
    playcount = 0

output = plays[playcount]
print "playing %s" % output
playcount = (playcount+1) % 9