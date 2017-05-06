import random

lose = 2
win = 1
tie = 0
unknown = -1
rpc = ['R','P','S']

if not input:
    last_outcome = unknown
    game_outcome = unknown
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    output = random.choice(rpc)
else:
    if last_outcome != unknown:
        grid[last_outcome][(rpc.index( last_input )-rpc.index( input ))%3] += 1
    
    last_outcome = game_outcome
    game_outcome = (rpc.index( input ) - rpc.index( output )) % 3
    last_input = input
    
    if grid[last_outcome][0] > grid[last_outcome][1]:
        if grid[last_outcome][0] > grid[last_outcome][2]:
            output = rpc[(rpc.index( input )+1)%3]
        else:
            output = rpc[rpc.index( input )]
    else:
        if grid[last_outcome][1] > grid[last_outcome][2]:
            output = rpc[(rpc.index( input )+2)%3]
        else:
            output = rpc[rpc.index( input )]
    
    if random.randint(0,15) == 0:
        for x in range(0, 2):
            for y in range(0, 2):
                grid[x][y] /= 4