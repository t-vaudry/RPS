if input=="":
    rWins=pWins=sWins=0
elif input=="R":
    if lastMove=="S":
        rWins+=1
elif input=="P":
    if lastMove=="R":
        pWins+=1
elif input=="S":
    if lastMove=="P":
        sWins+=1
if rWins>pWins and rWins>sWins:
    output=lastMove="P"
elif pWins>sWins:
    output=lastMove="S"
else:
    output=lastMove="R"