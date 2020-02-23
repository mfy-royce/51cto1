#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: basemath.py
@time:  11:46
@welcom to learn ai
"""


class Point():
    def __init__(self,*c):
        self.c =c

    def dist(self,p2):
        if  len(self.c) != len(p2.c):
            print('can not comput distance')
            return -1

        dist = 0
        for i1,i2 in zip(self.c,p2.c):
            if i1 < 0 or i2 < 0:
                dist = -1
                break
            dist += (i1 - i2) ** 2
        else:
            dist  =  dist ** 0.5
        return dist

p1 = Point(1,2,3,4,5)
p2 = Point(2,3,3,2,4)
print (p1.dist(p2))
print (p2.dist(p1))

class Vector(Point):
    def dot(self,v2):
        if len(self.c) !=len(v2.c):
            print("can not computer dot")
            return -1

        result =0
        for i1,i2 in zip(self.c,v2.c):
            if i1 < 0 or i2 < 0 :
                result =  -1
                break
            result += i1*i2
        return result


    def cosin(self,v2):
        zero = Point( * [0 for i in  range(len(self.c)) ] )
        dist1 = self.dist(zero)
        dist2 = v2.dist(zero)
        dot = self.dot(v2)
        result  = dot / (dist1 * dist2)
        return result

v1 = Vector(0,1)
v2 = Vector(1,0)
print(v2.cosin(v2))


