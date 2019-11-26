import numpy as np
import math

D = np.array([
    [5,5],
    [1,5],
    [4,5],
    [4.5,4],
    [5,1],
    [4.7,1]
])


def agnes(n):
    F = []
    L = np.zeros([len(D),len(D)])
    for i in range(len(D)):
        F.append([i])
        for j in range(len(D)):
            if i < j :
                L[i][j] = sum((D[i]-D[j])**2)
            else:
                L[i][j] = L[j][i]

    
    while len(F) > n:
        t = math.inf
        for i in range(len(F)-1):
            for j in range(i+1,len(F)):
                t2 = L[F[i]].T[F[j]]
                t2 = t2.sum() / (t2.shape[0] * t2.shape[1])
                if t2 < t:
                    t = t2
                    I = i
                    J = j
        F[I] = F[I] + F[J]
        F.remove(F[J])

    return F



print(agnes(3))