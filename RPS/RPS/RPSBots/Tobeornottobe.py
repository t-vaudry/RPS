if not input:
	tobeornottobe ='To be, or not to be, that is the question'
	tobeornottobe+='Whether tis nobler in the mind to suffer'
	tobeornottobe+='The slings and arrows of outrageous fortune,'
	tobeornottobe+='Or to take arms against a sea of troubles,'
	tobeornottobe+='And by opposing end them To die, to sleep,'
	tobeornottobe+='No more and by a sleep to say we end'
	tobeornottobe+='The heart-ache, and the thousand natural shocks'
	tobeornottobe+='That flesh is heir to tis a consummation'
	tobeornottobe+='Devoutly to be wished. To die, to sleep;'
	tobeornottobe+='To sleep, perchance to dream %u2013 ay, theres the rub:'
	tobeornottobe+='For in that sleep of death what dreams may come,'
	tobeornottobe+='When we have shuffled off this mortal coil,'
	tobeornottobe+='Must give us pause %u2013 theres the respect'
	tobeornottobe+='That makes calamity of so long life.'
	tobeornottobe+='For who would bear the whips and scorns of time,'
	tobeornottobe+='The oppressors wrong, the proud mans contumely,'
	tobeornottobe+='The pangs of disprized love, the laws delay,'
	tobeornottobe+='The insolence of office, and the spurns'
	tobeornottobe+='That patient merit of the unworthy takes,'
	tobeornottobe+='When he himself might his quietus make'
	tobeornottobe+='With a bare bodkin? Who would fardels bear,'
	tobeornottobe+='To grunt and sweat under a weary life,'
	tobeornottobe+='But that the dread of something after death,'
	tobeornottobe+='The undiscovered country from whose bourn'
	tobeornottobe+='No traveller returns, puzzles the will,'
	tobeornottobe+='And makes us rather bear those ills we have'
	tobeornottobe+='Than fly to others that we know not of?'
	tobeornottobe+='Thus conscience does make cowards of us all,'
	tobeornottobe+='And thus the native hue of resolution'
	tobeornottobe+='Is sicklied oer with the pale cast of thought,'
	tobeornottobe+='And enterprises of great pith and moment,'
	tobeornottobe+='With this regard their currents turn awry,'
	tobeornottobe+='And lose the name of action. Soft you now,'
	tobeornottobe+='The fair Ophelia! Nymph, in thy orisons'
	tobeornottobe+='Be all my sins remembered.'

	tobeornottobe = tobeornottobe.upper()
	n=0
	l=len(tobeornottobe)
else:
	n+=1

output = tobeornottobe[n%l]
while output!='R' and output!='P' and output !='S':
	n+=1
	output = tobeornottobe[n%l]