import random

#all possible combinations, for my turn and my opponent's


#which ones were chosen after pattern by opponent

if input == "":
    combine = { 'PP': '1', 
            'PR': '2', 
            'PS': '3',
            'RP': '4',
            'RS': '5',
            'RR': '6',
            'SS': '7',
            'SP': '8',
            'SR': '9',}
            
    split = {'1':'PP', 
              '2':'PR', 
              '3':'PS',
              '4':'RP',
              '5':'RS',
              '6':'RR',
              '7':'SS',
              '8':'SP',
              '9':'SR',}   
              
    anti = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    sequence = ""
    output = random.choice(["R","P","S"])
else:  
    
    if output != "":
        sequence += combine[output + input]

    for number in range(min(20, len(sequence)-1), 7, -1):
        pattern = sequence[-number:]
        index = sequence.find(pattern, 0, len(sequence) - 1)
        if index != -1:
            index += number
            choice = sequence[index]
            output = split[choice][1]
        else:
            pass
        
    else:
        output = random.choice(["R","P","S"])