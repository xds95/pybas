#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xds
# @wechat  : 551883614
# @file: show_the_path.py
# @time: 2019-03-06 11:48:11
# @Software: PyCharm


import numpy as np
import math


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    theta = np.asarray(theta)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2)
    b, c, d = -axis * math.sin(theta / 2)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


# v = [3, 5, 0]
# axis = [4, 4, 1]
# theta = 1.2
# print(np.dot(rotation_matrix(axis,theta), v))
# [ 2.74911638  4.77180932  1.91629719]

if __name__ == '__main__':
    v = [1, 0, 0]
    axis = [1, 1, 1]
    theta = np.pi / 2
    print(np.dot(rotation_matrix(axis, theta), v))
    # [ 2.74911638  4.77180932  1.91629719]
