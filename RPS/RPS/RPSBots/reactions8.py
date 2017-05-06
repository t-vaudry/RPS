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
        grid[game_outcome][(rpc.index( last_input )-rpc.index( input ))%3] += 1
    
    game_outcome = (rpc.index( input ) - rpc.index( output )) % 3
    last_input = input
    
    if grid[game_outcome][0] > grid[game_outcome][1]:
        if grid[game_outcome][0] > grid[game_outcome][2]:
            output = rpc[(rpc.index( input )+1)%3]
        else:
            output = rpc[rpc.index( input )]
    else:
        if grid[game_outcome][1] > grid[game_outcome][2]:
            output = rpc[(rpc.index( input )+2)%3]
        else:
            output = rpc[rpc.index( input )]
    
    if random.randint(0,63) == 0:
        for x in range(0, 2):
            for y in range(0, 2):
                grid[x][y] /= 4