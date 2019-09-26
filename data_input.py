import numpy
import pickle

data = {'c': 0, 'grad': 0}
#              A    B    C    D    E    F    G    H    I    L    M    N    O    P    R    S    T    U    V    Z
data['c'] = [[ 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 140, 118,   0,   0,  75], # A
            [  0,   0,   0,   0,   0, 211,  90,   0,   0,   0,   0,   0,   0, 101,   0,   0,   0,  85,   0,   0], # B
            [  0,   0,   0, 120,   0,   0,   0,   0,   0,   0,   0,   0,   0, 138, 146,   0,   0,   0,   0,   0], # C
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  75,   0,   0,   0,   0,   0,   0,   0,   0,   0], # D
            [  0,   0,   0,   0,   0,   0,   0,  86,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # E
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  99,   0,   0,   0,   0], # F
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # G
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  98,   0,   0], # H
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  87,   0,   0,   0,   0,   0,   0,  92,   0], # I
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  70,   0,   0,   0,   0,   0, 111,   0,   0,   0], # L
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # M
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # N
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 151,   0,   0,   0,  71], # O
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  97,   0,   0,   0,   0,   0], # P
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  80,   0,   0,   0,   0], # R
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # S
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # T
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 142,   0], # U
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0], # V
            [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]] # Z
data['d'] = [366,   0, 160, 242, 161, 178,  77, 151, 226, 244, 241, 234, 380,  98, 193, 253, 329,  80, 199, 374]

for ii in range(20):
    for jj in range(ii,20):
        if (ii != jj) & (data['c'][ii][jj] == 0):
            data['c'][ii][jj] = -1
        data['c'][jj][ii] = data['c'][ii][jj]


print(data['c'])
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)