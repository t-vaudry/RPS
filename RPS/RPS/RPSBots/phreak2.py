if input == "":
    output = "R"
    R_count = 0
    P_count = 0
    S_count = 0
elif input == "R":
    R_count +=1
    if ( R_count >= P_count and R_count >= S_count ):
       output == "P"
elif input == "P":
    P_count+=1
    if ( P_count >= R_count and P_count >= S_count ):
       output == "S"
elif input == "S":
    S_count+=1
    if ( S_count >= P_count and S_count >= R_count ):
       output == "R"