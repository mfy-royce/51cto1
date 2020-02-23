#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: sort.py
@time:  9:45
@welcom to learn ai
"""

from pythonds.test import randomList

def bubbleSort(iList):
    if  len(iList)<=1:
        return iList
    for i in range(len(iList),1,-1):        # len(iList)  -----> 2
        for j in range(len(iList)-1):
            if iList[j] > iList[j+1]:
                iList[j],iList[j+1] = iList[j+1],iList[j]
    return iList

def selectSort(iList):
    if len(iList)<=1 :
        return  iList
    for i in range(len(iList)-1):
        minIndex = i
        for j in range(i,len(iList)):
            if iList[minIndex] > iList[j]:
                minIndex = j
        iList[i],iList[minIndex] = iList[minIndex],iList[i]
    return  iList

def insertSort(iList):
    if len(iList)<=1 :
        return  iList
    for right in range(1,len(iList)):
        target = iList[right]
        for left in range(0,right):
            if target < iList[left]:
                iList[left+1:right+1] = iList[left:right]
                iList[left]  =target
                break
    return  iList



def mergeList(lList,rList):
    iList  = []
    left = 0
    right = 0
    while left <len(lList) and right < len(rList):
        if lList[left] > rList[right]:
            iList.append(rList[right])
            right += 1
        else:
            iList.append(lList[left])
            left += 1
    while left < len(lList):
        iList.append(lList[left])
        left += 1
    while right < len(rList):
        iList.append(rList[right])
        right += 1
    return iList

def mergeSort(iList):
    if len(iList)<= 1:
        return iList
    right = len(iList) // 2
    rList =mergeSort(iList[0:right])
    lList = mergeSort(iList[right:])
    iList = mergeList(lList,rList)
    return iList

def quickSort(iList):
    if len(iList)<= 1:
        return iList
    right =[]
    left = []
    for i in iList[1:]:
        if i >iList[0]:
            right.append(i)
        else:
            left.append(i)

    return quickSort(left) + [iList[0]] + quickSort(right)

def countingSort(iList):
    if len(iList)<= 1:
        return iList
    iLen = len(iList)
    rList = [None] *  iLen

    for i in range(iLen):
        small = 0
        same = 0
        for j in range(iLen):
            if iList[j] < iList[i]:
                small += 1
            if iList[j] == iList[i]:
                same += 1
        for k in range(small,small+ same):
            rList[k] = iList[i]
    return rList

if __name__ == '__main__':
    import timeit
    iList =  randomList(20)
    #iList = [57, 51, 2, 83, 22]
    #print("iList  is {}".format(iList))
    print(iList)
    # print(bubbleSort(iList))
    # print(timeit.timeit("bubbleSort(iList)","from __main__ import bubbleSort,iList",number =100))
    # print(selectSort(iList))
    # print(timeit.timeit("selectSort(iList)", "from __main__ import selectSort,iList", number=100))
    # print(insertSort(iList))
    # print(timeit.timeit("insertSort(iList)", "from __main__ import insertSort,iList", number=100))
    # print(mergeSort(iList))
    # print(timeit.timeit("mergeSort(iList)", "from __main__ import mergeSort,iList", number=100))
    # print(quickSort(iList))
    # print(timeit.timeit("quickSort(iList)", "from __main__ import quickSort,iList", number=100))
    print(countingSort(iList))
    print(timeit.timeit("countingSort(iList)", "from __main__ import countingSort,iList", number=100))
