#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: iris_knn_demo.py
@time:  14:47
@welcom to learn ai
"""


from ml.knn import KNN

def prepare_data():
    X=[]
    y=[]
    with open('iris.csv','r') as f:
        for i,e in enumerate(f.readlines()):
            e=e.split(',')
            if i ==0 :
                continue
            e = [s.strip() for s in e]
            e = [s.strip('"') for s in e]
            X.append([float(s) for s in e[1:5]])
            y.append(e[5])
    return X,y


if  __name__ == "__main__":
    X,y = prepare_data()
    model = KNN(5)
    model.fit(X,y)


    sample   =[5,3.4,1.5,0.2]
    print(model.predict(sample))