import random
import math

if input == "":
    move_char = ["P", "S", "R"]
    move_num = {'P':0, 'S':1, 'R':2}
    result = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    T = 0
    A = [0,0]
    B = [0,0]
    S = [0,0,0]
    R = [0,0,0]
    AMS = [[0 for j in range(3)] for i in range(54)]
    F = [[0 for j in range(3)] for i in range(81)]
    S_curr = 2
    R_curr = 0
    A_curr = random.choice([0,1,2])
    B_curr = 0
    output = move_char[A_curr]
else:
    def key_AMS(S,R):
        return 18*S[0] + 6*S[1] + 2*S[2] + int(R[0]+R[1]+R[2]>=0)

    def key_F(A,B):
        return 27*A[0] + 9*A[1] + 3*B[0] + B[1]

    def sample(wgt, s):
        w = [wgt[j]+s for j in range(len(wgt))]
        w0 = random.random() * reduce(lambda x, y: x+y, w, 0)
        j = 0
        W = w[0]
        while w0>W and j<len(w)-1:
            W = W+w[j]
            j = j+1
        return j

    def branch(AMS, S, R):
        i = key_AMS(S,R)
        f = AMS[i]
        w = [0.0, 0.0, 0.0]
        for j in range(len(f)):
            if f[j]>=0:
                w[j] = f[j]
            else:
                w[j] = math.exp(f[j])
        return sample(w, 0.1)

    def primary(F,A,B):
        return sample(F[key_F(A,B)], 0.1)
        
    B_curr = move_num[input]
    R_curr = result[B_curr][A_curr]
    if T >= 2:
        i = key_F(A,B)
        j = B_curr
        F[i][j] = F[i][j] + 1
        if T >= 3:
            i = key_AMS(S,R)
            j = S_curr
            AMS[i][j] = AMS[i][j] + R_curr
    R = [R_curr, R[0], R[1]]
    S = [S_curr, R[0], R[1]]
    A = [A_curr, A[0]]
    B = [B_curr, B[0]]
    if T>=27:
        S_curr = branch(AMS,S,R)
    else:
        S_curr = 2
    if S_curr==0:
        A_curr = (primary(F,A,B)+1)%3
    elif S_curr==1:
        A_curr = primary(F,A,B)
    else:
        A_curr = random.choice([0,1,2])
    T = T+1
    output = move_char[A_curr]