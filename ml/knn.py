# ! /usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: knn.py
@time:  18:50
@welcom to learn ai
"""
from ml.mathunit import Point


class KNN(object):
    def __init__(self, k=5):
        self.k = k

    def _k_nearest_neighbors(self, x):
        p = Point(x)
        distance = []
        for i, j in enumerate(self.X):
            p2 = Point(j)
            distance.append((p.dist(p2), self.y[i]))
        distance.sort(key=lambda x: x[0])
        return distance[:self.k]

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, x):
        ky = self._k_nearest_neighbors(x)
        k_dict = {}
        for dist,type in ky:
            if type in k_dict.keys():
                k_dict[type] +=1
            else:
                k_dict[type] = 0

        #k_dict = {'key1': 2, 'key2': 6, 'key3': 1}
        k_c = sorted(k_dict.items(),key= lambda  x :x[1],reverse=True)[0]
        return k_c[0]

if __name__ =="__main__":
    k_dict = {'key1': 2, 'key2': 6, 'key3': 1}
    k_c = sorted(k_dict.items(), key=lambda x: x[1], reverse=True)[0]
    print(k_c)