import random

if input=="" :
        player1_answers = [3]*1000
        num = -1
        List=[[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
        result = random.randint(0,3)
else:

  if input == "R" : 
        player1_answers[num] = 0
  elif input == "P" : 
        player1_answers[num] = 1
  else : 
        player1_answers[num] = 2

  if num<=2:
       result = random.randint(0,3)
  else:
       result = random.randint(0,3)
       I=player1_answers[num-2]
       J=player1_answers[num-1]
       if I==0 or I==1 or I==2 or J==0 or J==1 or J==2:
                A=player1_answers[num-3]
                B=player1_answers[num-2]
                C=player1_answers[num-1]
                List[A][B][C]+=1

                if max(List[I][J][0],List[I][J][1],List[I][J][2])==List[I][J][0]:
                    result = 1
                elif max(List[I][J][0],List[I][J][1],List[I][J][2])==List[I][J][1]:
                    result = 2
                elif max(List[I][J][0],List[I][J][1],List[I][J][2])==List[I][J][2]:
                    result = 0
num += 1

if result == 0: 
    output = "R"
elif result == 1: 
    output = "P"
else: 
    output = "S"