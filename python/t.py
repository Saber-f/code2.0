# 数集
minsup = 3
minconf = 5/7
D = [sorted(['牛奶','面包','薯片']),
sorted(['牛奶','面包','果汁']),
sorted(['牛奶','薯片','果汁']),
sorted(['牛奶','面包','薯片','奶酪']),
sorted(['牛奶','薯片','奶酪']),
sorted(['面包','果汁','奶酪']),
sorted(['牛奶','面包','薯片','果汁'])]

# 获取L1
def getL1():
    Ns = set({})
    for m in D:
        Ns = Ns | set(m)
    Ns = list(Ns)
    N = [0] * len(Ns)
    for m in D:
        for n in m:
            N[Ns.index(n)] = N[Ns.index(n)] + 1

    L1 = []
    for i in range(len(N)):
        if N[i] >= minsup:
            L1.append([Ns[i]])

    return L1

# 判断候选集的元素
def has_infrequent_subset(c,Lk_1):
    flage = True
    for i in c:
        c2 = c.copy()
        c2.remove(i)
        flage2 = False
        for j in Lk_1:
            if c2 == j:
                flage2 = True
                break
        if not flage2:
            flage = False
            break
    return flage

# 候选集产生
def apriori_gen(Lk_1):
    Ck = []
    for p in Lk_1:
        for q in Lk_1:
            flage = True
            for i in range(len(p)-1):
                if p[i] != q[i]:
                    flage = False
                    break
            if flage and p[-1] < q[-1]:
                c = p + [q[-1]] 
                if has_infrequent_subset(c,Lk_1):
                    Ck.append(c)
    return Ck

# 得到频繁项集
def Apriori():
    Lk_1 = getL1()
    while True:
        Ck = apriori_gen(Lk_1)    
        if len(Ck) == 0:
            break  
        N = [0] * len(Ck) 
        nc = 0
        for c in Ck:
            for d in D:
                if set(c) <= set(d):
                    N[nc] = N[nc] + 1
            nc = nc + 1

        for i in range(len(N)-1,-1,-1):
            if N[i] < minsup:
                Ck.remove(Ck[i])
        Lk_1 = Ck
    return Lk_1

# 计算置信度
def conf_(miniconf,Lk,s):
    L1 = []
    for i in s:
        L1 = L1 + [Lk[i]]
    L1 = set(L1)
    L2 = set(Lk) - L1
    n = 0
    m = 0
    for d in D:
        sd = set(d)
        if L1 < sd:
            n = n + 1
            if L2 < sd:
                m = m + 1
    if m/n >= miniconf:
        print(L1,'==>>',L2,'置信度:',m,'/',n,' ~ ',m/n)

    n = 0
    m = 0
    for d in D:
        sd = set(d)
        if L2 < sd:
            n = n + 1
            if L1 < sd:
                m = m + 1
    if m/n >= miniconf:
        print(L2,'==>>',L1,'置信度:',m,'/',n,' ~ ',m/n)

# 计算置信度
def conf(minconf,Lk):
    l = len(Lk)
    flage = False
    if l % 2 == 0:
        flage = True
    n = l // 2
    m = 1
    while m <= n:
        s = list(range(0,m))
        i = -1
        flage2 = True
        while flage2:
            conf_(minconf,Lk,s)
            while True:
                s[i] = s[i] + 1
                if s[i] <= l + i:
                    for j in range(i+1,0):
                        s[j] = s[j-1] + 1
                    i = -1
                    break
                else:
                    i = i - 1
                    if -i > m or (flage and -i == n):
                        flage2 = False
                        break
        m = m + 1


Lk = Apriori()
print('支持度不小于',minsup/len(D),'的频繁项集:',set(Lk[0]))
print()
conf(0,Lk[0])
print('\n置信度不小于',minconf)
conf(minconf,Lk[0])
                

