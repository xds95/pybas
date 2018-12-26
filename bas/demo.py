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

def fun(chromosome, dim=None, *, po_st=None, po_en=None):
    # 评价函数
    """
    :param chromosome: 点的位置
    :param dim: 数据点的数量
    :param bound: 边界
    :param po_st: 起始点
    :param po_en: 终点
    :param map_point: x暂时废弃x
    :return:
    """
    x = np.random.rand(dim)
    x[0:dim] = chromosome
    if all(x >= 0) and all(x <= 20):
        fitness = math.sqrt(pow(x[0] - po_st, 2) + 1)
        for i in range(0, dim-1):
            fitness += math.sqrt(pow(x[i+1] - x[i], 2) + 1)
        fitness += math.sqrt(pow(po_en - x[dim-1], 2) + 1)
        return fitness
    else:
        return 30  # 返回一个达不到的小/大值


bas = RBAS(fitness_function=fun, dim=20, steps=1000, eta=0.997, bound=[5, 15],
           step0=5, fitness_value=np.inf, po_st=10, po_en=10)
bas.run()
print(bas.gbest)
