import numpy as np
import geatpy as ea

class MyProblem(ea.Problem):            # 继承Problem父类
    def MyInit(self):
        car = np.array([[5,3],[10,10]]) # [[核载量],[车辆数值]]
        D = np.array

    def __init__(self):
        name = '派送路径'        # 初始化name
        M = 1                   # 初始化目标维数M
        maxormins = ‘1’         # 初始化目标最大最小值列表，1：min，-1：max
        Dim                     