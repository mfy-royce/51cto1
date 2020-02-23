#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: search.py
@time:  15:45
@welcom to learn ai
"""

from pythonds.test import randomList
from pythonds.sort import quickSort
import random


def sequentialSearch(iList,key):
    for i,num in enumerate(iList):
        if num == key:
            return i
    return -1

def binarySearch(iList,key):
    left  = 0
    right = len(iList)-1
    while right  - left >1:
        mid =  (right+left)//2
        if iList[mid] > key :
            right =mid-1
        elif iList[mid] <key :
            left = mid +1
        else:
            return mid
    if iList[right]== key:
        return right
    elif iList[left] == key:
        return left
    else:
        return -1

def insertSearch(iList,key):
    left = 0
    right = len(iList) - 1

    while right - left >1:
        if key > iList[right] or  key< iList[left]:
            return -1
        mid = left + (right - left ) * (key - iList[left]) // (iList[right] -iList[left])
        if key < iList[mid]:
            right = mid -1
        elif key > iList[mid]:
            left  =  mid +1
        else:
            return mid
    if key  == iList[right]:
        return right
    elif key == iList[left]:
        return left
    else:
        return -1


if __name__ =="__main__":
    for i in range(5):
        iList = quickSort(randomList(20))
        #iList = [4, 10, 12, 21, 37, 49, 50, 60, 66, 70, 76, 78, 80, 82, 87, 87, 88, 91, 96, 98]
        keys = [random.choice(iList),random.randrange(min(iList),max(iList))]
        #keys  = [27]
        for key in keys:
            print("iList is {}".format(iList))
            print("key is {}".format(key))
            res = insertSearch(iList,key)
            if res >=0:
                print("{} is in the list , index is {}".format(key,res))
            else:
                print("{} is not in the list".format(key))

