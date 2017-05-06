#DNA Polymerase
#This enzyme helps with DNA replication.
import random
if not input:
	telomere = 8
	DNA_strand1=""
	DNA_strand2=output = random.choice(['R','P','S'])
	base_pairs = ['R','R','R','R','S','S','S','S']
	nucleotide_frequency = range(8,0,-1)
else:
	for i in range(telomere):
		nucleotide_frequency[i]*=0.9
		if input==mRNA[i]:
			nucleotide_frequency[i]+=0.6
		elif input=={'R':'S', 'P':'R', 'S':'P'}[mRNA[i]]:
			nucleotide_frequency[i]-=0.5
		else:
			nucleotide_frequency[i]-=0.1
	j=30
	DNA_strand1+=input
	length = len(DNA_strand2)
	i = DNA_strand2.rfind(DNA_strand2[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = DNA_strand2.rfind(DNA_strand2[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		base_pairs[0] = base_pairs[2] = random.choice(['R','P','S'])
	else:
		base_pairs[0] = DNA_strand1[j+i]
		base_pairs[2] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
	j=30
	i = DNA_strand1.rfind(DNA_strand1[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = DNA_strand1.rfind(DNA_strand1[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		base_pairs[1] = base_pairs[3] = random.choice(['R','P','S'])
	else:
		base_pairs[1] = DNA_strand1[j+i]
		base_pairs[3] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
		
	for i in range(4,8):
		base_pairs[i] = {'R':'S','P':'R','S':'P'}[base_pairs[i-4]]
		
	output = {'R':'P', 'P':'S', 'S':'R'}[base_pairs[nucleotide_frequency.index(max(nucleotide_frequency))]]
	DNA_strand2+=output
mRNA = base_pairs