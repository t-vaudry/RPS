import math
import random

# a max of the best on the leaderboard...
# credit in full to the original authors

input = ''

class RPSPlayer:
    #               123456789.123456789.123456789.123456789.123456789.123456789.123456789.12
    DEFAULT_PLAY = "RSPRSPSSSSSSPSPRPPRPPSSPSSPPSSSPPRPPRPSPRSSSPSRRPRPSRPPRRSSSRRRPRRRRRSSP"
    SCORE = {"PR": 1, "RS": 1, "SP": 1, "RP": -1, "SR": -1, "PS": -1, "RR": 0, "SS": 0, "PP" : 0}
    
    KEYS = list(enumerate([[1,3,5,7], [2,4,6,8], [3,5,7], [4,6,8], [1,2,3,4], [2,3,4], [3,4], [1,3,5,7,9], [2,4,6,8,10]]))
    ADJ  = {1: [0, 1, 0], -1: [0, 0, 1], 0: [1, 0, 0]}
   
    def __init__(self):
        self.round = 0
        self.hist_us   = ""
        self.hist_them = ""
        self.hist_pred = "SSSSSS"
        self.weighting  = [9, 1 , 0] # win, block, reverse
        self.memory = {}
        self.score = 0
        self.memory_length = 5

    def default_for_round(self):
        return self.DEFAULT_PLAY[self.round % 72]
        
    def tally_score(self):
        last_round = self.hist_us[-1:] + self.hist_them[-1:]
        #print last_round
        self.score += self.SCORE[last_round]
        #
        last_result = self.SCORE[self.hist_pred[-1:] + self.hist_them[-1:]]
        adjustment  = self.ADJ[last_result]
        for i in range(3):
            self.weighting[i] += adjustment[i]

            
        
    def get_keys(self):
        def get_segment(s):
            # !!TODO suggests that it is about time to change this structure...
            if s == 1: return self.hist_them[len(self.hist_them) - 1]
            if s == 2: return self.hist_us  [len(self.hist_us  ) - 1]
            if s == 3: return self.hist_them[len(self.hist_them) - 2]
            if s == 4: return self.hist_us  [len(self.hist_us  ) - 2]
            if s == 5: return self.hist_them[len(self.hist_them) - 3]
            if s == 6: return self.hist_us  [len(self.hist_us  ) - 3]
            if s == 7: return self.hist_them[len(self.hist_them) - 4]
            if s == 8: return self.hist_us  [len(self.hist_us  ) - 4]
            if s == 9: return self.hist_them[len(self.hist_them) - 5]
            if s ==10: return self.hist_us  [len(self.hist_us  ) - 5]
        
        for key_no, segment in self.KEYS:
            key = str(key_no) + ':'
            for s in segment:
                key += get_segment(s)
            yield key
    
    def remember_opponent(self, move):
        
        def add_key(key, move):
            # !!TODO forgetfullness so that
            # we do not get trained into a strategy...
            if key not in self.memory:
                 self.memory[key] = {"R": 0, "P": 0, "S": 0}
            self.memory[key][move] += 1
            #print self.hist_us
            #print self.hist_them
            #print key, move, self.memory[key]
        
        if len(self.hist_them) > self.memory_length:
            for key in self.get_keys():
                add_key(key, move)
        
        self.hist_them += move
        
        if self.round % 500 == 0:
           for key in self.memory:
               self.memory[key]["R"] /= 2
               self.memory[key]["P"] /= 2
               self.memory[key]["S"] /= 2
    
    def remember_me(self, move):
        self.hist_us += move

    def dump(self):
        print self.memory
        print 'weighting: ', self.weighting
        print self.hist_us
        print self.hist_them
        print self.hist_pred
        print "score", self.score
    
    def predict(self):
        
        def find(key):
            if key not in self.memory:
                 return {"R": 0, "P": 0, "S": 0}
            return self.memory[key]

        pr = pp = ps = 0
        for key in self.get_keys():
            value = find(key)  
            pr +=  value["R"]
            pp +=  value["P"]
            ps +=  value["S"]
        
        if pr == pp == ps == 0:
            return self.default_for_round()
        
        prediction = random.choice("R" * pr + "P" * pp + "S" * ps)
        self.hist_pred += prediction
        
        if random.random() < .95:
            return {"R" : "P", "P" : "S", "S" : "R"}[prediction]
        else:
            return prediction

    def next(self, last_move):
        if last_move != "":
            self.remember_opponent(last_move)
            self.tally_score()
        if len(self.hist_us) < self.memory_length:
            result = self.default_for_round()
        else:
            result = self.predict()
        self.round += 1
        self.remember_me(result)
        return result

####################################################################################################
# Similar to switching3, but a different strategy selection:
# always use best performed strategy
####################################################################################################

if input == "":
  dna = ""
  opp = []

  anti_expected = {'P': 'S', 'S': 'R', 'R': 'P'}
  dna_encode = {'PP': '1', 'PR': '2', 'PS': '3', 'RP': '4', 'RS': '5','RR': '6','SS': '7','SP': '8', 'SR': '9',}
  dna_decode = {'1':'PP', '2':'PR', '3':'PS','4':'RP','5':'RS','6':'RR','7':'SS','8':'SP','9':'SR',}
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  output1 = random.choice(["R", "P", "S"])

  index = random.randint(0,2)
  candidates = [output1] * 3
  performance = [0, 0, 0]
  total = 0
else:
  dna += dna_encode[input + output]
  opp.append(input)
  sc = score[output+input]
  total += sc

  for i in range(3):
     s = score[candidates[i]+input]
     if s == -1:
       performance[i] = 0
     elif s == 1:
       performance[i] += 1
     elif total < 0 and s == 0:
       performance[i] = 0

  m = max(performance)
  bestlist = [i for i, c in enumerate(performance) if c == m] 
  index = random.choice(bestlist)

  candidates[0] = anti_expected[random.choice(opp)]
  candidates[1] = anti_expected[random.choice(opp)]
  candidates[2] = anti_expected[random.choice(opp)]

  for length in range(min(4, len(dna)-1), 0, -1):
    search = dna[-length:]
    idx = dna.rfind(search, 0, -1)
    if idx != -1:
      answered = dna_decode[dna[idx + length]]
      candidates[1] = anti_expected[answered[0]]
      candidates[2] = anti_expected[anti_expected[answered[1]]]
      break

  output1 = candidates[index]

##################################################################################################

##################################################################################################
#DNA Polymerase
#This enzyme helps with DNA replication.
##################################################################################################



if not input:
    limit = 11
    telomere = 30
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
    output3 = random.choice(['R','P','S'])
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
    historase+=input
    historase+=output
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
    if length>50:
        guess=str(historase[l-endonuclease])
        for i in range(-endonuclease+1,0):
            guess = guess+str(historase[l+i])
        if guess in phosphodiester:
            base_pairs[27] = max(phosphodiester[guess], key = lambda x: phosphodiester[guess].get(x) )
        else:
            base_pairs[27] = random.choice(['R','P','S'])
            
        for i in range(28,30):
            base_pairs[i] = {'R':'S','P':'R','S':'P'}[base_pairs[i-1]]
    else:
        for i in range(27,30):
            nucleotide_frequency[i] = 0
            
        
    output3 = {'R':'P', 'P':'S', 'S':'R'}[base_pairs[nucleotide_frequency.index(max(nucleotide_frequency))]]
    output3 = {0:output3,1:random.choice(['R','P','S'])}[ random.random() < 0.2 or max(nucleotide_frequency)<0 ]
mRNA = base_pairs



if input == "":
    player = RPSPlayer()

output2 = player.next(input)

output = random.choice([output1, output2, output3])