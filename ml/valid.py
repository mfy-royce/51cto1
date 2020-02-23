#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: valid.py
@time:  14:29
@welcom to learn ai
"""
import random
from ml.metrics import Metrics
def cross_valid(model,X,y,split,precision):
    train_X, train_y, test_X, test_y = split(X,y)
    model.fit(train_X,train_y)
    y_pred = [model.predict(x) for x in test_X]
    return precision(test_y,y_pred)

def train_test_split(X,y,ratio =0.2):
    train_X,train_y,test_X,test_y= [],[],[],[]
    for i,j in zip(X,y):
        rand  = random.uniform(0.0,1.0)
        if ratio < rand :
            train_X.append(i)
            train_y.append(j)
        else:
            test_X.append(i)
            test_y.append(j)
    return train_X,train_y,test_X,test_y

if __name__ == '__main__':
    from iris_knn_demo import prepare_data
    from knn import KNN
    X,y = prepare_data()

    model = KNN()
    from functools import partial
    spliter = partial(train_test_split,ratio=0.2)
    p_score = cross_valid(model,X,y,spliter,Metrics.precision)
    print(p_score)
