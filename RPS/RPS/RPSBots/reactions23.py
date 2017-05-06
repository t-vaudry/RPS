import random

lose = 2
win = 1
tie = 0
unknown = -1
rps = ['R','P','S']

if not input:
    game_outcome = unknown
    grid = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
    output = random.choice(rps)
    lose_count = 0
else:
    input_index = rps.index( input )
    if game_outcome != unknown:
        grid[game_outcome][(input_index-last_input_index)%3] += 1.0
    
    game_outcome = (input_index - rps.index( output )) % 3
    if game_outcome == win:
        lose_count += 1
    else:
        lose_count = 0
    
    if grid[game_outcome][0] > grid[game_outcome][1]:
        if grid[game_outcome][0] > grid[game_outcome][2]:
            greatest_index = 0
        else:
            greatest_index = 2
    else:
        if grid[game_outcome][1] > grid[game_outcome][2]:
            greatest_index = 1
        else:
            greatest_index = 2
    
    last_input_index = input_index
    output = rps[(input_index+greatest_index+1)%3]
    
    if random.randint(0,64-1) == 0 or lose_count == 8:
        for x in range(0, 3):
            for y in range(0, 3):
                grid[x][y] /= 8.0