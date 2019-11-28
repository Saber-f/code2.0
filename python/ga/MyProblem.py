import numpy as np
import geatpy as ea
import networkx as nx
import matplotlib.pyplot as plt

class MyProblem(ea.Problem):              # 继承Problem父类
    def getD(self,node_list,edge_list):
        G = nx.Graph()
        for node in node_list:
            G.add_node(node)
        for edge in edge_list:
            G.add_edge(edge[0],edge[1],weight=edge[2])
            G.add_edge(edge[1],edge[0],weight=edge[2])
        p = nx.shortest_path(G)             # 各点到各点的最短路径
        d = nx.shortest_path_length(G)      #各点到各点的最短间距离
        d = dict(d)
        return d,p

    def MyInit(self):
        self.car = np.array([[5,3],[10,10]])        # [[核载量],[车辆数值]]
        self.need = np.array(\
            [1,7,0.8,1.3,2.8,1.9,3.5,0.9,0.3,1.2])  # 各点需求量
        node_list = ['A','B','C','D','E',\
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
        self.D,self.P = self.getD(node_list,edge_list,9)      # 最短路邻接

    def __init__(self):
        self.MyInit()
        name = '派送路径'                                # 初始化name
        M = 1                                           # 初始化目标维数M
        maxormins = [1]                                 # 初始化目标最大最小值列表，1：min，-1：max
        Dim = self.need.size + self.car.shape[1] - 2    # 决策变量维数
        varTypes = [1] * Dim                            # 决策变量类型（0：连续，1：离散）
        lb = [0] * Dim                                  # 决策变量下界
        up = list(range(size(self.need),1,-1)) + list(slef.car[1,1:-1])   #决策变量上界
        lbin = [1] * Dim        # 决策变量下边界
        ubin = [1] * Dim        # 决策变量上边界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):     # 目标函数，pop为传入种群对象
        Vars = pop.Phen         # 得到决策变量矩阵
        V2 = Vars.copy()
        for v in Vars:



             
problem = MyProblem()           # 实例化问题对象