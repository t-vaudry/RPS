#RNA Polymerase
#This enzyme helps with RNA replication, so that the two resultant strands
#are RNA_strand1 and RNA_strand2 respectively.
import random
if not input:
	RNA_strand1=""
	RNA_strand2=output = random.choice(['R','P','S'])
else:
	j=100
	RNA_strand1+=input
	length = len(RNA_strand2)
	i = RNA_strand2.find(RNA_strand2[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = RNA_strand2.find(RNA_strand2[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		output = random.choice(['R','P','S'])
	else:
		output = RNA_strand1[j+i]
	
	output = {'R':'P', 'P':'S', 'S':'R'}[output]
	RNA_strand2+=output