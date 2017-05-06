#DNA Polymerase
#This enzyme helps with DNA replication.
import random
if not input:
	limit = 11
	telomere = 33
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
	phosphodiester = dict()
	historase = ""
	endonuclease = 8
	exoplastase = 0.825
	phosphodiester2 = dict()
	historase2 = ""
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
	j=limit
	DNA_strand1+=input
	DNA_strand2+=output
	historase+=input+output
	historase2+=output+input
	DNA_strand3+=deoxyribonuclease[input+output]
	DNA_strand0+=ribonuclease[input+output]
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
		base_pairs[1] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
	j=limit
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
		base_pairs[3] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
	j=limit
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
		base_pairs[5] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
	j=limit
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
		base_pairs[7] = {'R':'P','P':'S','S':'R'}[DNA_strand2[j+i]]
		
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
	
	#Adenosine triphosphate
	l=len(historase)
	if l >= endonuclease+2:
		codon = str(historase[l-endonuclease-2])
		for i in range(-endonuclease-1,-2):
			codon = codon+str(historase[l+i])
		if not codon in phosphodiester:
			phosphodiester[codon] = dict()
		if historase[l-1] in phosphodiester[codon]:
			phosphodiester[codon][historase[l-1]]+=1
		else:
			phosphodiester[codon][historase[l-1]]=1
		
		codon = str(historase2[l-endonuclease-2])
		for i in range(-endonuclease-1,-2):
			codon = codon+str(historase2[l+i])
		if not codon in phosphodiester2:
			phosphodiester2[codon] = dict()
		if historase2[l-1] in phosphodiester2[codon]:
			phosphodiester2[codon][historase2[l-1]]+=1
		else:
			phosphodiester2[codon][historase2[l-1]]=1
	if length>50:
		guess=str(historase[l-endonuclease])
		for i in range(-endonuclease+1,0):
			guess = guess+str(historase[l+i])
		if guess in phosphodiester:
			base_pairs[27] = max(phosphodiester[guess], key = lambda x: phosphodiester[guess].get(x) )
		else:
			base_pairs[27] = random.choice(['R','P','S'])
		guess=str(historase2[l-endonuclease])
		for i in range(-endonuclease+1,0):
			guess = guess+str(historase2[l+i])
		if guess in phosphodiester2:
			base_pairs[30] = max(phosphodiester2[guess], key = lambda x: phosphodiester2[guess].get(x) )
			base_pairs[30] = {'R':'S','P':'R','S':'P'}[base_pairs[30]]
		else:
			base_pairs[30] = random.choice(['R','P','S'])
			
		for i in [28,29,31,32]:
			base_pairs[i] = {'R':'S','P':'R','S':'P'}[base_pairs[i-1]]
	else:
		for i in range(27,33):
			nucleotide_frequency[i] = 0
			
		
	output = {'R':'P', 'P':'S', 'S':'R'}[base_pairs[nucleotide_frequency.index(max(nucleotide_frequency))]]
	output = {0:output,1:random.choice(['R','P','S'])}[ random.random() < 0.2 or max(nucleotide_frequency)<0 ]
mRNA = base_pairs