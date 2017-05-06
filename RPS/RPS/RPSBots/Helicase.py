#Helicase
#This enzyme helps with DNA replication.
import random
if not input:
	telomere = 2
	base_pairs = range(telomere)
	for i in range(telomere):
		base_pairs[i] = random.choice(['R','P','S'])
	nucleotide_frequency = range(telomere,0,-1)
	helicase=[0,0,0,0,0,0]
	output = random.choice(['R','P','S'])
else:
	for i in range(telomere):
		nucleotide_frequency[i]*=0.87
		if input==mRNA[i]:
			nucleotide_frequency[i]+=telomere*0.5
		elif input=={'R':'S', 'P':'R', 'S':'P'}[mRNA[i]]:
			nucleotide_frequency[i]-=telomere*0.48
		else:
			nucleotide_frequency[i]-=telomere*0.02
		
	#Helicase
	helicase[0] = helicase[0]*0.95+{'R':0,'P':-0.1,'S':0.1}[output]
	helicase[1] = helicase[1]*0.95+{'R':0.1,'P':0,'S':-0.1}[output]
	helicase[2] = helicase[2]*0.95+{'R':-0.1,'P':0.1,'S':0}[output]
	base_pairs[0] = {0:'R',1:'P',2:'S',3:'R',4:'P',5:'S'}[helicase.index(max(helicase[0:3]))]
	
	helicase[3] = helicase[3]*0.95+{'R':0.1,'P':0,'S':-0.1}[input]
	helicase[4] = helicase[4]*0.95+{'R':-0.1,'P':0.1,'S':0}[input]
	helicase[5] = helicase[5]*0.95+{'R':0,'P':-0.1,'S':0.1}[input]
	base_pairs[1] = {0:'R',1:'P',2:'S',3:'R',4:'P',5:'S'}[helicase.index(max(helicase[3:6]))]
		
	output = {'R':'P', 'P':'S', 'S':'R'}[base_pairs[nucleotide_frequency.index(max(nucleotide_frequency))]]
	output = {0:output,1:random.choice(['R','P','S'])}[ random.random() < 0.2 or max(nucleotide_frequency)<0 ]
mRNA = base_pairs