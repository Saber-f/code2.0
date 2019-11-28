import numpy as np
import geatpy as ea
import networkx as nx
import matplotlib.pyplot as plt

class MyProblem(ea.Problem):            # 继承Problem父类
    def getD(self,node_list,edge_list):
        G = nx.Graph()
        for node in node_list:
            G.add_node(node)
        for edge in edge_list:
            G.add_edge(edge[0],dege[1],dege[2])
            G.add_edge(edge[1],dege[0],dege[2])
        p = nx.shortest_path()

        
        return 


    
    def MyInit(self):
        self.car = np.array([[5,3],[10,10]])        # [[核载量],[车辆数值]]
        self.need = np.array(\
            [1,7,0.8,1.3,2.8,1.9,3.5,0.9,0.3,1.2])  # 各点需求量
        node_list = 'ABCDEFGHIJP'                   # 节点标签(最前面的点与需求量对应，最后一个点为配送中心，中专点在中间)
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
        ]                                    # 边列表
        D = self.getD(node_list,edge_list)   # 最短路邻接

    def __init__(self):
        self.MyInit()
        name = '派送路径'        # 初始化name
        M = 1                   # 初始化目标维数M
        maxormins = [1]         # 初始化目标最大最小值列表，1：min，-1：max
        Dim = self.need.size + self.car.shape[1] - 2  # 决策变量维数
             
problem = MyProblem()   # 实例化问题对象