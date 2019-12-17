import math

# 数据
D = [
    ['fine','hot','hight','no','no'],
    ['fine','hot','hight','yes','no'],
    ['cloudy','hot','hight','no','yes'],
    ['rain','warmth','hight','no','yes'],
    ['rain','cool','normal','no','yes'],
    ['rain','cool','normal','yes','no'],
    ['cloudy','cool','normal','yes','yes'],
    ['fine','warmth','hight','no','no'],
    ['fine','cool','normal','no','yes'],
    ['rain','cool','normal','no','yes'],
    ['fine','cool','normal','yes','yes'],
    ['cloudy','warmth','hight','yes','yes'],
    ['cloudy','hot','normal','no','yes'],
    ['rain','warmth','hight','yes','no']
]

D2 = [
    ['cloudy','cool','hight','yes','?'],
    ['fine','hot','normal','yes','?']
]

def getD(L,W):
    D2 = []
    for l in L:
        t = []
        for w in W:
            t.append(D[l][w])
        D2.append(t.copy())
    return D2

def H(L,W,n,Mt):
    '''
    计算熵/Gini指数
    '''
    D = getD(L,W)
    Z = {}
    for d in  D:
        if d[-1] in Z:
            Z[d[n]] = Z[d[n]] + 1
        else:
            Z[d[n]] = 1

    L = list(Z.values())
    s = sum(L)
    HX = 0
    for l in L:
        if Mt == 'ID3' or Mt == 'C4.5':
            HX = HX - l/s * math.log(l/s)
        elif Mt == 'CART':
            HX = HX + l/s * (1 - l/s)
        else:
            print('方法错误')
            HX = 0
    return HX

def TH(L,W,Y,X,Mt):
    '''
    计算条件熵H(Y|X)，Gini指数
    '''
    D = getD(L,W)
    Z = {}
    for d in  D:
        if d[X] in Z:
            Z[d[X]] = Z[d[X]] + 1
        else:
            Z[d[X]] = 1
    
    
    LX =list(Z.values())
    sx = sum(LX)
    HX = 0
    HL = []
    NL = []
    LL = []
    ZL = []
    for t in list(Z.keys()):
        ZY = {}
        t2 = []
        t3 = 0
        for d in D:
            if d[X] == t:
                t2.append(t3)
                t4 = d[Y]
                if d[Y] in ZY:
                    ZY[d[Y]] = ZY[d[Y]] + 1
                else:
                    ZY[d[Y]] = 1
            t3 = t3 + 1
        LY = list(ZY.values())
        s = sum(LY)
        HY = 0
        for l in LY:
            if Mt == 'ID3' or Mt == 'C4.5':
                HY = HX - l/s * math.log(l/s)
            elif Mt == 'CART':
                HY = HX - l/s * (1 - l/s)
            else:
                print('方法错误')
                HY = 0
        HX = HX + Z[t]/sx * HY
        HL.append(HY)
        NL.append(t)
        LL.append(t2)
        ZL.append(t4)
    return HX,HL,NL,LL,ZL

def Spanning_tree(L,W,n,Mt):
    tH = H(L,W,n,Mt)
    if tH == 0:
        D = getD(L,W)
        return  D[0][n]
    
    t1 = -math.inf
    for i in range(len(W)):
        if i != n:
            tTH = TH(L,W,n,W[i],Mt)[0]
            if Mt == 'ID3':
                t2 = tH - tTH
            elif Mt == 'C4.5':
                t2 = (tH - tTH) / tH
            elif Mt == 'CART':
                t2 = tTH
            else:
                print('方法错误2')
                return {}
            if t2 > t1:
                t1 = t2
                I = i
    HL,HL,NL,LL,ZL = TH(L,W,n,W[I],Mt)
    Z = {}
    for i in range(len(LL)):
        for j in range(len(LL[i])):
            LL[i][j] = L[LL[i][j]]

    for i in range(len(HL)):
        if HL[i] != 0:
            W2 = W.copy()
            del W2[I]
            Z[NL[i]] = Spanning_tree(LL[i],W2,n-1,Mt)
        else:
            Z[NL[i]] = ZL[i]
    Z['ID'] = W[W[I]]   #嵌套，想不到吧
    return Z 
  
def fennei(D,Z):
    for i in range(len(D)):
        t = Z[D[i][Z['ID']]]
        while type(t) == dict:
            t = t[D[i][t['ID']]]
        D[i][-1] = t
    return D

Z = Spanning_tree(list(range(len(D))),list(range(len(D[0]))),len(D[0])-1,'ID3')
D2_ = fennei(D2.copy(),Z)
print('ID3::')
print(Z)
print(D2_)

print('C45::')
Z = Spanning_tree(list(range(len(D))),list(range(len(D[0]))),len(D[0])-1,'C4.5')
D2_ = fennei(D2.copy(),Z)
print(Z)
print(D2_)

print('CART::')
Z = Spanning_tree(list(range(len(D))),list(range(len(D[0]))),len(D[0])-1,'CART')
D2_ = fennei(D2.copy(),Z)
print(Z)
print(D2_)