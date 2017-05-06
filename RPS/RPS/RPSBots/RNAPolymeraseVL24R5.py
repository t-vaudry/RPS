#RNA Polymerase
#This enzyme helps with RNA replication, so that the two resultant strands
#are RNA_strand1 and RNA_strand2 respectively.
import random
if not input:
	RNA_strand1=""
	RNA_strand2=""
	output = random.choice(['R','P','S'])
	ribonuclease = {'RP':'I','PS':'A','SR':'M','PR':'S','SP':'U','RS':'P','RR':'E','PP':'R','SS':'B'}
else:
	j=24
	RNA_strand1+=input
	RNA_strand2+=ribonuclease[input+output]
	length = len(RNA_strand2)
	if j>length:
		j=length
	i = RNA_strand2.rfind(RNA_strand2[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = RNA_strand2.rfind(RNA_strand2[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length or random.random() < 0.2:
		output = random.choice(['R','P','S'])
	else:
		output = {'R':'P', 'P':'S', 'S':'R'}[RNA_strand1[j+i]]