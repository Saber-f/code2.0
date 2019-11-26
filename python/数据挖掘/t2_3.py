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


def pAB(n):
    l = len(D)
    Z = {'ID':n,'num':len(D)}
    for i in range(l):
        if D[i][n] in Z:
            Z[D[i][n]]['num'] = Z[D[i][n]]['num'] + 1
            for j in range(len(D[0])-1):
                if D[i][j] in Z[D[i][n]][j]:
                    Z[D[i][n]][j][D[i][j]] = Z[D[i][n]][j][D[i][j]] + 1
                else:
                    Z[D[i][n]][j][D[i][j]] = 1
        else:
            Z[D[i][n]] = {'num':1}
            for j in range(len(D[0])-1):
                Z[D[i][n]][j] = {D[i][j]:1}


    return Z



def fenlei(D2,Z):
    
    Z2 = {}

    for d in  D2:
        Z2[D2.index(d)] = {}
        for i in Z:
            if i != 'ID' and i != 'num':
                Z2[D2.index(d)][i] = Z[i]['num'] #/ Z['num']
                for j in Z[i]:
                    if j != 'num':
                        flage = True
                        for k in Z[i][j]:
                            if k == d[j]:
                                Z2[D2.index(d)][i] = Z2[D2.index(d)][i] * Z[i][j][k] #/ Z[i]['num']
                                flage = False
                                break
                        if flage:
                            Z2[D2.index(d)][i] = 0
                            break
        t = 0
        for i in Z2[D2.index(d)]:
            if Z2[D2.index(d)][i] > t:
                t = Z2[D2.index(d)][i]
                D2[D2.index(d)][Z['ID']] = i

    return D2





Z = pAB(len(D[0])-1)
print(Z)
print(fenlei(D2.copy(),Z))