# Bobby Compact Test
# I'm new to this kind of thing...

import random

if input == "R": # Predict S or P.
	output = "S"
elif input == "S": # Predict R or P.
	output = "P"
elif input == "P": # Predict R or S.
	output = "R"

output = random.choice(["R", "S", "P"])