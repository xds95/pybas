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
    # 随机生成的
    y = np.random.rand(dim*3//2)
    # chromosome = np.hstack((np.reshape(self.xnums, (self.dim // 2, 1)),
    #                         np.reshape(self.chromosome, (self.dim // 2, 2)))).ravel()
    xnums = np.arange(po_st[0], po_en[0], (po_en[0] - po_st[0]) / (dim / 2))
    chromosome = np.hstack((np.reshape(xnums, (dim // 2, 1)), np.reshape(chromosome, (dim // 2, 2)))).ravel()
    y[0:dim*3//2] = chromosome
    # length_y = pow(500 / dim, 2)
    # if all(y >= 0) and all(y <= 500):
    # fitness = math.sqrt(pow(y[0] - po_st[1], 2) + pow(y[1]-po_st[2]+pow(y[2]-po_st[3])))
    fitness = 0
    for i in range(0, dim*3//2 // 3):
        # i represent points' position, and dim+1//3 must be positive integer
        # pos_ceil = np.ceil(y[i]).astype(int)
        # pos_floor = np.floor(y[i]).astype(int)
        # if map_Can[pos_ceil, np.ceil(i*500/dim).astype(int)] > 80 or \
        #         map_Can[pos_floor, np.floor(i*500/dim).astype(int)] > 80:
        j = 3 * i
        if y[j + 1] > 500 or y[j + 1] < 0 or y[j] > 500 or y[j] < 0:
            fitness += 500
        elif y[j + 2] < map_Can[y[j].astype(int), y[j + 1].astype(int)] or y[j + 2] > 60:
        # elif y[j + 2] < 120 or y[j + 2] > 200:
            fitness += 500

        if i == 0:
            fitness += math.sqrt(pow(y[j] - po_st[0], 2) + pow(y[j + 1] - po_st[1], 2) + pow(y[j + 2] - po_st[2], 2))
        else:
            fitness += math.sqrt(pow(y[j] - y[j - 3], 2) + pow(y[j + 1] - y[j - 2], 2) + pow(y[j + 2] - y[j - 1], 2))

        if i == dim // 3 - 1:
            fitness += math.sqrt(pow(y[j] - po_en[0], 2) + pow(y[j + 1] - po_en[1], 2) + pow(y[j + 2] - po_en[2], 2))

    return fitness

# 地图编号
map_id = 1
# load地图
map_Can = np.loadtxt('../map/scenario_a%s/map.txt' % map_id, dtype=int)
# 对bas进行赋值
bas = RBAS(fitness_function=fun, dim=24, steps=50000, eta=0.999951, bound=[100, 500],
           step0=30, fitness_value=np.inf, po_st=[400, 0, 50], po_en=[0, 500, 0],
           map_Can=map_Can)
# 运行rum
bas.run()
# 打印
print(np.reshape(bas.gbest_chromosome, (bas.dim // 2, 3)))
print(bas.gbest_fitness_value)
ch = np.reshape(bas.gbest_chromosome.astype(int), (bas.dim//2, 3))
print(map_Can[ch[..., 0], ch[..., 1]])

# bas.fitness(chromosome=bas.gbest_chromosome)
stp = STP(1, bas)
stp.show_map()
