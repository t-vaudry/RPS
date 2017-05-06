import random
if not input:
  output=random.choice("RPS")
  history=""
else:
  history+=input
  output=random.choice(history)