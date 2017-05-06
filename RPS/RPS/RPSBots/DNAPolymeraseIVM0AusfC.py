#DNA Polymerase
#This enzyme helps with DNA replication.
import random
if not input:
	limit = 6
	telomere = 27
	DNA_strand0=""
	DNA_strand1=""
	DNA_strand2=""
	DNA_strand3="" #Unlike most other DNA, this one has four strands
	base_pairs = range(telomere)
	for i in range(telomere):
		base_pairs[i] = random.choice(['R','P','S'])
	nucleotide_frequency = range(telomere,0,-1)
	helicase=[0,0,0,0,0,0]
	deoxyribonuclease = {'RP':'a','PS':'a','SR':'a','PR':'b','SP':'b','RS':'b','RR':'c','PP':'c','SS':'c'}
	ribonuclease = {'RP':'I','PS':'A','SR':'M','PR':'S','SP':'U','RS':'P','RR':'E','PP':'R','SS':'B'}
	output = random.choice(['R','P','S'])
else:
	for i in range(telomere):
		if input==mRNA[i]:
			nucleotide_frequency[i]+=1
		elif input=={'R':'S', 'P':'R', 'S':'P'}[mRNA[i]]:
			nucleotide_frequency[i]=0
	DNA_strand1+=input
	DNA_strand2+=output
	DNA_strand3+=deoxyribonuclease[input+output]
	DNA_strand0+=ribonuclease[input+output]
	length = len(DNA_strand2)
	j=limit
	if j>length:
		j=length
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
		base_pairs[1] = {'R':'S', 'P':'R', 'S':'P'}[DNA_strand2[j+i]]
	j=limit
	if j>length:
		j=length
	i = DNA_strand1.rfind(DNA_strand1[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = DNA_strand1.rfind(DNA_strand1[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		base_pairs[2] = base_pairs[3] = random.choice(['R','P','S'])
	else:
		base_pairs[2] = DNA_strand1[j+i]
		base_pairs[3] = {'R':'S', 'P':'R', 'S':'P'}[DNA_strand2[j+i]]
	j=limit
	if j>length:
		j=length
	i = DNA_strand0.rfind(DNA_strand0[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = DNA_strand0.rfind(DNA_strand0[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		base_pairs[4] = base_pairs[5] = random.choice(['R','P','S'])
	else:
		base_pairs[4] = DNA_strand1[j+i]
		base_pairs[5] = {'R':'S', 'P':'R', 'S':'P'}[DNA_strand2[j+i]]
	j=limit
	if j>length:
		j=length
	i = DNA_strand3.rfind(DNA_strand3[length-j:length-1],0,length-2)
	while i==-1:
		j-=1
		i = DNA_strand3.rfind(DNA_strand3[length-j:length-1],0,length-2)
		if j<2:
			break
	if i==-1 or j+i>=length:
		base_pairs[6] = base_pairs[7] = random.choice(['R','P','S'])
	else:
		base_pairs[6] = DNA_strand1[j+i]
		base_pairs[7] = {'R':'S', 'P':'R', 'S':'P'}[DNA_strand2[j+i]]
		
	for i in range(8,24):
		base_pairs[i] = {'R':'S','P':'R','S':'P'}[base_pairs[i-8]]
		
	base_pairs[26] = random.choice(['R','P','S'])
		
	#Helicase
	helicase[0] = helicase[0]*0.95+{'R':0,'P':-0.1,'S':0.1}[DNA_strand2[length-1]]
	helicase[1] = helicase[1]*0.95+{'R':0.1,'P':0,'S':-0.1}[DNA_strand2[length-1]]
	helicase[2] = helicase[2]*0.95+{'R':-0.1,'P':0.1,'S':0}[DNA_strand2[length-1]]
	base_pairs[24] = {0:'R',1:'P',2:'S',3:'R',4:'P',5:'S'}[helicase.index(max(helicase[0:3]))]
	
	helicase[3] = helicase[3]*0.95+{'R':0.1,'P':0,'S':-0.1}[input]
	helicase[4] = helicase[4]*0.95+{'R':-0.1,'P':0.1,'S':0}[input]
	helicase[5] = helicase[5]*0.95+{'R':0,'P':-0.1,'S':0.1}[input]
	base_pairs[25] = {0:'R',1:'P',2:'S',3:'R',4:'P',5:'S'}[helicase.index(max(helicase[3:6]))]
		
	output = {'R':'P', 'P':'S', 'S':'R'}[base_pairs[nucleotide_frequency.index(max(nucleotide_frequency))]]
	if max(nucleotide_frequency)<0:
		output = random.choice(['R','P','S'])
mRNA = base_pairs