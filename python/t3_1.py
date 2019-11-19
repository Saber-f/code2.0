import random
import math
import numpy as np

D = [
    [1,1],
    [2,1],
    [1,2],
    [2,2],
    [4,3],
    [5,3],
    [4,4],
    [5,4]
]

def k_means(D,n):
    # n个聚类中心
    z = random.sample(range(len(D)),n)
    D = np.array(D)
    Z = D[z]
    Z2 = np.copy(Z)
    s = np.array(range(len(D)))
    F = np.zeros(len(D))
    
    while True:
        for d in range(len(D)):
            t = np.sum((Z - D[d])**2,1)
            F[d] = list(t).index(np.min(t))

        for i in range(n):
            Z2[i] = D[s[F == i]].mean(0)

        if (Z == Z2).all():
            break
        Z = np.copy(Z2)

    Z = []
    for i in range(n):
        Z.append(list(s[F == i]))

    return Z
            
print(k_means(D.copy(),2))