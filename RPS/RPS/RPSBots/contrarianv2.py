import random
if input == "":
    count_in = [1.0, 1.0, 1.0]
    count_out = [1.0, 1.0, 1.0]
else:
    for i in range(3):
        count_in[i] *= 0.7
        count_out[i] *= 0.7
    if input == "R":
        count_in[0] += 1
    elif input == "P":
        count_in[1] += 1
    elif input == "S":
        count_in[2] += 1
s1 = sum(count_in)
s2 = sum(count_out)
p1 = [count_in[0]/s1, count_in[1]/s1, count_in[2]/s1]
p2 = [count_out[0]/s2, count_out[1]/s2, count_out[2]/s2]
p3 = [p1[0]*(1-p2[0]), p1[1]*(1-p2[1]), p1[2]*(1-p2[2])]
if random.random() < p3[0] / sum(p3):
    output = "P"
    count_out[1] += 1
elif random.random() < p3[1] / sum(p3[1:]):
    output = "S"
    count_out[2] += 1
else:
    output = "R"
    count_out[0] += 1