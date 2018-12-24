#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo.py
# @time: 2018/8/30 2:49
# @Software: PyCharm

from bas.rbas import RBAS
import math
import numpy as np


# 使用前请安装文件
# pip install pybas
# 确保版本号大于0.0.1

# 求 z = -cos(x) - sin(y)(x in [1, 2*pi], y in [1, 2*pi]) 的最大值

def fun(vars, po_st=18, po_en=18):
    # 评价函数
    # x, y = vars
    # x = np.array(range(0, 11))
    x = np.random.rand(11)
    x[0:11] = vars
    if all(x >= 0 ) and all(x <= 36):
    # return -np.cos(x) - np.sin(y) + 10
        fitness = 0
        fitness = math.sqrt(pow(x[0] - po_st, 2) + 1)

        for i in range(0, 10):
            fitness += math.sqrt(pow(x[i+1] - x[i], 2) + 1)

        fitness += math.sqrt(pow(po_en - x[10], 2)+ 1 )
        return fitness
    else:
        return 100  # 返回一个达不到的小/大值


bas = RBAS(fitness_function=fun, dim=11, steps=1000, eta=0.997,
           bound=[0, 10], step0=3, fitness_value=np.inf)
bas.run()
print(bas.gbest)
