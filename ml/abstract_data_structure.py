#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: abstract_data_structure.py
@time:  20:17
@welcom to learn ai
"""
class Point(object):
    def __init__(self,cor):
        self.cor =cor

    def dist(self,p2):
        if  len(self.cor) != len(p2.cor):    # 检查 长度 相等
            print('can not comput distance')
            return -1

        dist = 0
        for i1,i2 in zip(self.cor,p2.cor):
            if i1 < 0 or i2 < 0:           #检查 坐标为正
                dist = -1
                break
            dist += (i1 - i2) ** 2
        else:
            dist  =  dist ** 0.5
        return dist

class Vector(Point):
    def norm(self):
        o = Vector([0 for i in self.cor])
        return self.dist(o)

    def dot(self,v2):
        result =  0
        for i1,i2  in zip(self.cor,v2.cor):
            result  += i1 * i2
        return result

    def cosin(self,v2):
        #return self.dot(v2)
        return  self.dot(v2) / (self.norm() * v2.norm())