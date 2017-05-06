if not input:
 h=""
 input="R"
h+=input
import random
output={'R':'P','P':'S','S':'R'}[random.choice(h)]