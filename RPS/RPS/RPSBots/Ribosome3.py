#Ribosome
#This organelle reads some RNA and outputs a protein!
import random, math
if not input:
	peptide=""
	RNA_strand=""
	output=random.choice(['R','P','S'])
	amino_acids={
	'RP': 'R',
	'PS': 'I',
	'SR': 'B',
	'PR': 'O',
	'SP': 'S',
	'RS': '0',
	'RR': 'M',
	'PP': 'E',
	'SS': 'X'}
	length=0
else:
	j=4
	RNA_strand+=input
	peptide+=amino_acids[input+output]
	length+=1
	protein=[0,0,0]
	output=random.choice(['R','P','S'])
	dynein = peptide.count(peptide[length-j-1:length-1])
	while dynein>10:
		tryptophan=length-2
		isomer=math.pow(j+1,math.log(j+1)+1)
		for i in range(dynein):
			tryptophan = peptide.rfind(peptide[length-j-1:length-1],0,tryptophan)
			if j+tryptophan<length and not tryptophan == -1:
				protein[0]+={'R':isomer,'P':-isomer,'S':0}[RNA_strand[tryptophan+j]]
				protein[1]+={'R':0,'P':isomer,'S':-isomer}[RNA_strand[tryptophan+j]]
				protein[2]+={'R':-isomer,'P':0,'S':isomer}[RNA_strand[tryptophan+j]]
		j+=1
		dynein = peptide.count(peptide[length-j-1:length-1])
	if protein!=[0,0,0]:
		output={0:'P',1:'S',2:'R'}[protein.index(max(protein))]