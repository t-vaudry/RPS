import random
com = 0
ans = ['R','P','S']
usr_results = []
ran = 3
def calc():
    r = usr_results.count(0)
    p = usr_results.count(1)
    s = usr_results.count(2)
    if r > p and r > s:
        return 1
    elif p > s:
        return 2
    else:
        return 0
global com
global num
choice = random.sample(range(ran), 1)
if choice[0] == 3:
    com = num
elif choice[0] != 3:
    com = choice[0]
if com == 0:
    output = ans[0]
elif com == 1:
    output = ans[1]
elif com == 2:
    output = ans[2]
usr = input
if usr == ans[0]:
    usr = 0
elif usr == ans[1]:
    usr = 1
else:
    usr = 2
usr_results.append(usr)
if len(usr_results) >= 4:
    global num
    num = calc()
    ran = 4