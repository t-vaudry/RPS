import random

#Assuming that the opponents next selection is biased by the current selection and response,
#attempt to estimate a transition function that maps current state to next response

#Previous version randomized between a "winning" move and a "draw" move in order to reduce predictability but #it might be reducing the match win ratio.



if (input == ""):

    #All things being equal
    T_r = {};
    T_s = {};
    T_p = {};
	
    T_r["RR"] = 1;
    T_r["RP"] = 1;
    T_r["RS"] = 1;
    T_r["SR"] = 1;
    T_r["SP"] = 1;
    T_r["SS"] = 1;
    T_r["PR"] = 1;
    T_r["PP"] = 1;
    T_r["PS"] = 1;
	
    T_p["RR"] = 1;
    T_p["RP"] = 1;
    T_p["RS"] = 1;
    T_p["SR"] = 1;
    T_p["SP"] = 1;
    T_p["SS"] = 1;
    T_p["PR"] = 1;
    T_p["PP"] = 1;
    T_p["PS"] = 1;
	
    T_s["RR"] = 1;
    T_s["RP"] = 1;
    T_s["RS"] = 1;
    T_s["SR"] = 1;
    T_s["SP"] = 1;
    T_s["SS"] = 1;
    T_s["PR"] = 1;
    T_s["PP"] = 1;
    T_s["PS"] = 1;

    oldInput = "R";
    oldOutput = "R";
    output = "R";

else:

	if (oldInput <> ""):
		if (input == "R"):
			T_r[oldInput+oldOutput] += 1;
		elif (input == "P"):
 			T_p[oldInput+oldOutput] += 1;
		elif (input == "S"):
			T_s[oldInput+oldOutput] += 1;


#Now attempt to select the best response from the transition table

	oldInput = input;
	oldOutput = output;


	if (T_r[input+output] > T_p[input+output]) and (T_r[input+output] > T_s[input+output]):
		output = "P";
	elif (T_p[input+output] > T_r[input+output]) and (T_p[input+output] > T_s[input+output]):
		output = "S"
	elif (T_s[input+output] > T_r[input+output]) and (T_s[input+output] > T_p[input+output]):
		output = "R"
        else:
                output = random.choice(["R","S","P"]);