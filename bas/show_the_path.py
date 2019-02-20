#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xds
# @wechat  : 551883614
# @file: show_the_path.py
# @time: 2018-12-26 15:42:34
# @Software: PyCharm


import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import numpy as np


class ShowThePath(object):
    """Plot the map information and planned path.

    :Attributes:


    """

    def __init__(self,
                 map_id,
                 bas):
        """
        :param map_id: 地图的编号
        :param bas: 包含了已经规划好的一切信息
        """
        self.map_id = map_id
        self.path_point = bas.gbest.chromosome
        """
        :2D实验中：我们获得一条路径，其y步进，z固定，只有x在进行规划
        :3D实验中：获得一组数据点g.best,编码方式可以为X1Y1Z1...XnYnZn,或者X1X2...Zn-1Zn
        """
        self.path_x = (self.path_point * 100 / 36).astype(np.int)
        self.path_y = np.arange(0, 100, 100 / 30, dtype='uint8').transpose()
        self.path_z = np.arange(79, 80, 1 / 30, dtype='uint8').transpose()

    def show_map(self):
        """

        :return:
        :raise: 此处将地图和散点绘制在一张图之后，散点只能选整数，尚未分析出原因
        """
        _x = np.arange(0, 100, 0.2)
        _y = np.arange(0, 100, 0.2)
        _z = np.loadtxt('/Users/xds/PycharmProjects'
                        '/pybas/map/scenario_a%s/map.txt' % self.map_id)
        _trace0 = go.Surface(
            colorscale='Earth',
            x=_x,
            y=_y,
            z=_z)
        _map = [_trace0]
        _trace1 = {
            "x": self.path_x,
            "y": self.path_y,
            "z": self.path_z,
            "mode": "markers+lines",
            "name": "The planned path of UAVs",
            "type": "scatter3d",
            "uid": "f1ef8e"
        }
        _path = [_trace1]
        _layout = {
            "autosize": True,
            "height": 514,
            "scene": {
                "aspectratio": {
                    "x": 1,
                    "y": 1,
                    "z": 1
                },
                "camera": {
                    "center": {
                        "x": 0,
                        "y": 0,
                        "z": 0
                    },
                    "eye": {
                        "x": 0.503072648931,
                        "y": 0.549958943385,
                        "z": -2.03272306783
                    },
                    "up": {
                        "x": 0,
                        "y": 0,
                        "z": 1
                    }
                },
                "xaxis": {
                    "title": "CCG",
                    "type": "category"
                },
                "yaxis": {
                    "title": "Life Expectancy",
                    "type": "linear"
                },
                "zaxis": {
                    "title": "Smokers per 1000",
                    "type": "linear"
                }
            },
            "title": "3d Line Plot",
            "width": 1099,
            "xaxis": {
                "title": "CCG",
                "type": "category"
            },
            "yaxis": {
                "title": "Life Expectancy",
                "type": "linear"
            }
        }
        _fig = Figure(data=_map + _path, layout=_layout)
        py.plot(_fig)

    def show_obstacle(self):
        pass


STP = ShowThePath

if __name__ == '__main__':
    x, y, z = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 400).transpose()

    trace1 = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=12,
            color=z,  # set color to an array/list of desired values
            colorscale='Viridis',  # choose a colorscale
            opacity=0.8
        )
    )

    data = [trace1]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    fig = go.Figure(data=data, layout=layout)
    # py.iplot(fig, filename='3d-scatter-colorscale')
    py.plot(fig)
