import math
import random
# this bot is an accurate representation of
# what would happen if lava became holy and played RPS

if not input:
    heat = 0
    cooldown = 0
    terrain = "PSPRRPS"
if (random.randint(1,10) == 10):
    cooldown = random.randint(1,10)
output = terrain[heat%7]
if (cooldown < 0):
    heat += 1
else:
    heat += 5
    cooldown -= 1