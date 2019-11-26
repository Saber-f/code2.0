import numpy as np 
import random

D = np.array([
    [0,1,2,2,3],
    [1,0,2,4,3],
    [2,2,0,1,4],
    [2,4,1,0,3],
    [3,3,4,3,0]
])

def k_medoids(n):
    # n个聚类中心
    z = random.sample(range(len(D)),n)
    s = np.array(range(len(D)))
    Z = s[z]
    Z2 = np.copy(Z)
    F = np.zeros(len(D))
    
    while True:
        for d in range(len(D)):
            F[d] = list(D[d][Z]).index(np.min(D[d][Z]))

        for i in range(n):
            t = sum(D[F==i].T[F==i])
            Z2[i] = s[F==i][list(t).index(min(t))]

        if (Z == Z2).all():
            break
        Z = np.copy(Z2)

    Z = []
    for i in range(n):
        Z.append(list(s[F == i]))

    return Z





print(k_medoids(2))

