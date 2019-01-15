#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: demo.py
# @time: 2018/8/30 2:49
# @Software: PyCharm

from bas.rbas import RBAS
from bas.show_the_path import STP
import math
import numpy as np


# 求一个函数的最小值


def fun(chromosome, dim=None, *, po_st=None, po_en=None, map_Can=None):
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
    # TODO:
    # 完成剩余参数的添加
    # 添加障碍物是否碰撞的判断
    y = np.random.rand(dim)
    y[0:dim] = chromosome
    if all(y >= 0) and all(y <= 20):
        fitness = math.sqrt(pow(y[0] - po_st, 2) + 1)
        for i in range(0, dim - 1):
            pos_ceil = np.ceil(y[i + 1]*500/36).astype(int)
            pos_floor = np.floor(y[i + 1]*500/36).astype(int)
            if map_Can[pos_ceil, i] > 80 or map_Can[pos_floor, i] > 80:
            # if map_Can[i, pos_ceil] > 60 or map_Can[i, pos_floor] > 60:
                fitness += 50
            fitness += math.sqrt(pow(y[i + 1] - y[i], 2) + 1)
        fitness += math.sqrt(pow(po_en - y[dim - 1], 2) + 1)
        return fitness
    else:
        # 边界限制
        c = 50 + sum(0 < i < 20 for i in y) * 50
        return c  # 返回一个达不到的小/大值


map_id = 1
map_Can = np.loadtxt('/Users/xds/PycharmProjects/pybas/map'
                     '/scenario_a%s/map.txt' % map_id)
bas = RBAS(fitness_function=fun, dim=30, steps=999, eta=0.997, bound=[5, 15],
           step0=5, fitness_value=np.inf, po_st=10, po_en=10, map_Can=map_Can)
bas.run()
print(bas.gbest)

# stp = STP(1, bas)
# stp.show_map()
