#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: metrics.py
@time:  13:49
@welcom to learn ai
"""


class  Metrics(object):     # 度量
    @classmethod
    def precision(cls,y,y_pred):   # 精确度
        cnt = 0
        for y1,y2 in zip(y,y_pred):
            if y1  == y2 :
                cnt +=1
        return cnt / len(y)


if __name__ == '__main__':
    y = [1,2,3]
    y_pred = [1,2,4]
    print( Metrics.precision(y,y_pred) )