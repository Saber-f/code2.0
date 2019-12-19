import numpy as np
import geatpy as ea
import networkx as nx

class MyProblem(ea.Problem):              # 继承Problem父类
    def getD(self,node_list,edge_list):
        G = nx.Graph()
        G.add_nodes_from(node_list)
        for edge in edge_list:
            G.add_edge(edge[0],edge[1],weight=edge[2])
        nx.shortest_simple_paths
        p = nx.shortest_path(G,weight='weight')             # 各点到各点的最短路径
        d = nx.shortest_path_length(G,weight='weight')      # 各点到各点的最短间距离
        d = dict(d)
        return d,p

    def MyInit(self):
        self.max_time = 8 * 60                      # 单次配送任务时间限制8h
        self.max_mileage = 35                       # 单次最大里程
        self.unload_time = 5                        # 卸货用时
        self.speed = 6                              # 货车平均行驶速度(min/km)
        self.car = np.array([[5,2,3],[1,2,2]])          # [[核载量],[车辆数数目]]
        self.car_kinds = self.car[0].size           # 货车的种类
        self.need = np.array(\
            [1.7,0.8,1.3,2.8,1.9,3.5,0.9,0.3,1.2])  # 各点需求量
        self.node_list = ['A','B','C','D','E',\
            'F','G','H','I','J','P']                # 节点标签(最前面的点与需求量对应，最后一个点为配送中心，中专点在中间)
        edge_list = [
            ['P','A',5],
            ['P','B',8],
            ['P','C',7],
            ['P','J',5],
            ['P','E',4],
            ['P','F',12],
            ['P','G',9],
            ['P','H',12],
            ['P','I',6],
            ['A','B',4],
            ['A','I',3],
            ['B','C',3],
            ['C','D',4],
            ['C','J',5],
            ['D','J',2],
            ['D','E',3],
            ['E','J',2],
            ['E','F',10],
            ['F','H',7],
            ['F','G',4],
            ['G','H',5],
            ['H','I',9]
        ]                                           # 边列表
        self.D,self.P = self.getD(self.node_list,edge_list)      # 最短路邻接

    def __init__(self):
        self.MyInit()
        name = '货物配送方案求解'
        M = 3                                           # 初始化目标维数M(货车里程，配送完成耗时，满载率)
        maxormins = [1,1,-1]                            # 初始化目标最大最小值列表，1：min，-1：max
        Dim = self.need.size * 2 - 1                    # 决策变量维数
        varTypes = [1] * Dim                            # 决策变量类型（0：连续，1：离散）
        lb = [0] * Dim                                  # 决策变量下界
        ub = list(range(self.need.size-1,0,-1)) + \
            [self.car_kinds-1] * self.need.size         # 决策变量上界
        lbin = [1] * Dim                                # 决策变量下边界
        ubin = [1] * Dim                                # 决策变量上边界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)


    def get_SK(self,V):                         # 解析v得到配送顺序S和使用的车种类K两个列表
        t = list(range(self.need.size))
        S = [0] * self.need.size
        K = [0] * self.need.size
        for i in range(self.need.size - 1):
            S[i] = t[int(V[i])]
            del t[int(V[i])]
            K[i+1] = int(V[i+self.need.size])
        S[-1] = t[0]
        K[0] = int(V[self.need.size-1])
        return S,K

    def aimFunc(self, pop):                     # 目标函数，pop为传入种群对象
        Vars = pop.Phen                         # 得到决策变量矩阵
        Y = np.zeros([pop.sizes,3])             # 函数值
        CV = np.zeros([pop.sizes,1])            # 限制必须配送完
        for i in range(pop.sizes):              # 计算每个个体的目标函数值
            S,K = self.get_SK(Vars[i])          # s配送点顺序，k货车种类
            #  开始配送
            mileage = 0                         # 已行驶里程
            time = 0                            # 配送已耗时
            delivery = 0                        # 已配送货物量
            time_record = []                    # 每辆车运行总时长记录
            for j in self.car[1]:
                time_record.append([0]*j)
            s_ = -1                             # 出发点为配送中心
            si = 0
            s = S[si]
            actual_cargo_capacity = 0           # 实际载货量
            while True:
                t = self.D[self.node_list[s_]][self.node_list[s]] \
                    + self.D[self.node_list[s]][self.node_list[-1]]         # 从上一个配送点到次配送点并返回的路程
                mileage_ = mileage + t                                      # 累计里程
                time_ = time + t * self.speed + self.unload_time            # 累计配送时间
                delivery_ = delivery + self.need[s]
                if mileage_ <= self.max_mileage and time_ <= \
                    self.max_time and delivery_ <= self.car[0][K[0]]:       # 到该配送点后返回配送中心，里程不超过35km;时间不超过8h;累计配送量不超过货车载重量;
                    mileage = mileage + self.D[self.node_list[s_]][self.node_list[s]]       
                    time = time + self.D[self.node_list[s_]][self.node_list[s]] * self.speed + 5
                    delivery = delivery + self.need[s]
                    actual_cargo_capacity = actual_cargo_capacity + self.need[s]
                    s_ = s
                    si = si + 1
                    if si == len(S):
                        flage1 = True
                        break
                    s = S[si]
                else:                                                       # 如果不满足限制条件，此车返回配送中心，换下一辆车
                    Y[i][0] = Y[i][0] + mileage + \
                        self.D[self.node_list[s_]][self.node_list[-1]]                      # 总里程
                    Y[i][2] = Y[i][2] + self.car[0][K[0]]                   # 理论总载货量
                    t = time_record[K[0]].index(min(time_record[K[0]]))
                    time_record[K[0]][t] = time_record[K[0]][t] + time + self.D[self.node_list[s_]][self.node_list[-1]] * 6
                    if len(K) == 1:                                         # 最后一辆车
                        flage1 = False
                        break
                    mileage = 0
                    time = 0
                    delivery = 0
                    s_ = -1
                    del K[0]                                                # 换下一辆车
            if flage1:
                Y[i][0] = Y[i][0] + mileage + \
                    self.D[self.node_list[s_]][self.node_list[-1]]          # 总里程
                Y[i][2] = Y[i][2] + self.car[0][K[0]]                       # 理论总载货量
                t = time_record[K[0]].index(min(time_record[K[0]]))
                time_record[K[0]][t] = time_record[K[0]][t] + time + self.D[self.node_list[s_]][self.node_list[-1]] * 6
            Y[i][2] = actual_cargo_capacity / Y[i][2]                       # 满载率
            Y[i][1] = max(max(time_record))                                 # 全部配送完成耗时
            CV[i][0] = sum(self.need) - actual_cargo_capacity

        pop.CV = np.hstack([CV])
        pop.ObjV = Y

    def mywrite(self,file_name,list):
        f1 = open(file_name,'w')
        for i in list:
            for j in i:
                f1.write(str(j))
                f1.write('\t')
            f1.write('\n')
        f1.close()

    def saveAns(self,pop):
        S = []
        K = []
        for v in pop.Phen:
            s,k = self.get_SK(v)
            S.append(s)
            K.append(k)
        ANS = []
        for i in range(len(S)):
            flage = True
            for ans in ANS:         # 去重
                if pop.ObjV[i][0] == ans[-3] and pop. ObjV[i][1] == ans[-2] and pop.ObjV[i][2] == ans[-1]:
                    flage = False
                    break
            if flage:
                ANS.append(S[i] + [-1] + K[i] + [-1] + list(pop.ObjV[i])) 
        self.mywrite('ANS.txt',ANS)




## 实例化种群对象         
problem = MyProblem()       # 实例化问题对象

## 种群设置
Encoding = 'RI'             # 编码方式
NIND = 100                  # 种群规模

Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges,
    problem.borders)        # 创建区域描述器
# 实例化种群对象（此时种群还没有被真正初始化，仅仅是生成一个种群对象）
population = ea.Population(Encoding, Field, NIND)


## 算法参数设置
# 实例化一个算法模板对象
myAlgorithm = ea.moea_NSGA3_templet(problem, population)
myAlgorithm.MAXGEN = 500        # 最大遗传代数
myAlgorithm.drawing = 0         # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制过程动画）

## 调用算法模板进行种群进化
NDSet = myAlgorithm.run()       # 执行算法模板
problem.saveAns(NDSet)          # 保存结果