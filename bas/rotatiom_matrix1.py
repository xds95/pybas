#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xds
# @wechat  : 551883614
# @file: show_the_path.py
# @time: 2019-03-06 11:48:11
# @Software: PyCharm


import numpy as np
import math


# 输入旋转后的终点，中间得到一个转换矩阵，输出一个新的矩阵
def rotation_matrix(end_point):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    end_point = np.asarray(end_point)
    end_point = end_point / math.sqrt(np.dot(end_point, end_point))
    theta_y = math.atan2(end_point[0], end_point[2])
    theta_x = math.atan2(end_point[1], end_point[2])
    theta_z = math.atan2(end_point[1], end_point[0])
    r11 = math.cos(theta_z)*math.cos(theta_z) - math.sin(theta_x)*math.sin(theta_y)*math.sin(theta_z)
    r12 = - math.cos(theta_x)*math.sin(theta_z)
    r13 = math.sin(theta_y)*math.cos(theta_z) + math.sin(theta_x)*math.cos(theta_y)*math.sin(theta_z)
    r21 = math.cos(theta_y)*math.sin(theta_z) + math.sin(theta_x)*math.sin(theta_y)*math.cos(theta_z)
    r22 = math.cos(theta_x)*math.cos(theta_z)
    r23 = math.sin(theta_y)*math.sin(theta_z) - math.sin(theta_x)*math.cos(theta_y)*math.cos(theta_z)
    r31 = -math.cos(theta_x)*math.sin(theta_y)
    r32 = math.sin(theta_x)
    r33 = math.cos(theta_x)*math.cos(theta_y)
    R = [[r11, r12, r13], [r21, r22, r23], [r31, r32, r33]]
    return np.array(R)
    # axis = np.asarray(axis)
    # theta = np.asarray(theta)
    # axis = axis / math.sqrt(np.dot(axis, axis))
    # a = math.cos(theta / 2)
    # b, c, d = -axis * math.sin(theta / 2)
    # aa, bb, cc, dd = a * a, b * b, c * c, d * d
    # bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    # return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
    #                  [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
    #                  [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


if __name__ == '__main__':
    v = [1, 1, 1]
    axis = [1, 1, 1]
    print(np.dot(rotation_matrix(axis), v))
