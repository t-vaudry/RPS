import random

lose = 2
win = 1
tie = 0
unknown = -1
rpc = ['R','P','S']

if not input:
    game_outcome = unknown
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    output = random.choice(rpc)
else:
    if game_outcome != unknown:
        grid[game_outcome][(rpc.index( input )-rpc.index( last_input ))%3] += 1
    
    game_outcome = (rpc.index( input ) - rpc.index( output )) % 3
    
    
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
    
    last_input = input
    output = rpc[(rpc.index( input )+greatest_index+1)%3]
    
    if random.randint(0,64) == 0:
        for x in range(0, 3):
            for y in range(0, 3):
                grid[x][y] /= 2