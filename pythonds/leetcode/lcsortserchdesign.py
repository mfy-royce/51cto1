#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lcsortserchdesign.py
@time:  12:09
@welcom to learn ai
"""


def merge(list1,list2):
    index1 = 0
    index2 = 0
    # len1 = len(list1)
    # len2 = len(list2)
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] > list2[index2]:
            list1.insert(index1, list2[index2])
            index1 += 1
            index2 += 1
        else:
            index1 += 1

    while index1 == len(list1) and index2 < len(list2):
        list1.insert(index1, list2[index2])
        index1 += 1
        index2 += 1
    return list1


def isBadVersion(n):
    firstBadVersion =  4
    if n<4:
        return False
    else:
        return True

def firstBadVersion(n=5):
    left =1
    right =n
    badVersion = -1

    while right - left >=0:
        mid  =  (left+ right) // 2
        if isBadVersion(mid):
            badVersion = mid
            right =mid -1
        else:
            left = mid +1
    return badVersion

import random
class solution():
    def __init__(self,nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        cNums = self.nums.copy()
        rNums = []
        while len(cNums):
            index = random.choice(range(len(cNums)))
            rNums.append(cNums.pop(index))
        return rNums

class MinStack():
    def __init__(self):
        self.stack =[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        try:
            self.stack.pop()
        except Exception as e:
            pass

    def top(self):
        try:
            return self.stack[-1]
        except Exception as e:
            return None

    def getMin(self):
        try:
            return min(self.stack)
        except Exception as e:
            return None



if __name__=="__main__":
    from pythonds.test import randomList, showLink, creatLink, creatCycleLink, showCyscleLink

    l1 = sorted(randomList(5))
    l2 = sorted(randomList(5))
    l1 = [6, 16, 27, 47, 51]
    l2 = [29, 41, 56, 84, 92]
    print (l1)
    print( l2)
    print("merge result is {}".format(merge(l1,l2)))

    print("firstBadVersionrge result is {}".format(firstBadVersion(100)))

    # obj = solution([1,2,3])
    # print("obj is {}".format(obj))
    # print("shuffle is {}".format(obj.shuffle()))
    # print("reset is {}".format(obj.reset()))
    # print("shuffle is {}".format(obj.shuffle()))

    obj = MinStack()
    print("obj is {}".format(obj))
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print("getMin is {}".format(obj.getMin()))
    obj.pop()
    print("top is {}".format(obj.top()))
    print("getMin is {}".format(obj.getMin()))

