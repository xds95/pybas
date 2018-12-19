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

def fun(vars):
    # 评价函数
    # x, y = vars
    x = np.array(range(0, 11))
    x[0:11] = vars
    if 0 <= x.any() <= 10:
    # return -np.cos(x) - np.sin(y) + 10
        fitness = 0
        for i in range(0, 10):
            fitness += math.sqrt(pow(x[i+1] - x[i], 2) + 1)
        return fitness

    else:
        return 1000  # 返回一个达不到的小/大值


bas = RBAS(fitness_function=fun, dim=11, steps=11100, eta=0.9997,
           bound=[0, 10], step0=3, fitness_value=np.inf)
bas.run()
print(bas.gbest)
