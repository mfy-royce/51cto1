#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: array.py
@time:  22:06
@welcom to learn ai
"""

def removeDuplicates(iList):
    left = 1
    for right in range(1,len(iList)):
        if iList[right-1] == iList[right]:
            right += 1
        else:
            iList[left] = iList[right]
            left +=1
            right += 1
    return left

def maxProfit_back(iList):
    buy = 0
    profit = 0
    for i in range(1 , len(iList)):
        if iList[i-1] < iList[i] and buy ==0:
            buy =1
            inPrice = iList[i-1]
            print("buyIndex is {},price is {}".format(i-1,inPrice))
        elif iList[i-1] > iList[i] and buy == 1:
            buy = 0
            profit += iList[i-1] - inPrice
            print("sellIndex is  {},price is {},profit is  {}".format(i-1,iList[i-1],profit))
        if buy == 1 and i == len(iList)-1 :
            profit += iList[i] - inPrice
            print("sellIndex is  {},price is {},profit is  {}".format(i, iList[i], profit))
    return profit
#
def maxProfit(iList):
    profit = 0
    maxPro  = 0
    for i,num in enumerate(iList):
        if i>0:
            profit = num - iList[i-1]

        if profit > 0:
            maxPro += profit
    return maxPro

def rotate_back(iList,k):
    if k <= 0:
        return iList
    for i in range(k):
        temp  =  iList[-1]
        iList[1:] = iList[0:-1]
        iList[0] = temp
    return iList

def rotate(iList,k):
    k = k % len(iList)
    f = len(iList) - k
    if k <= 0:
        return iList
    iList[-f:], iList[0:-f] = iList[0:f], iList[f:]
    return iList

def containsDuplicate(iList):
    iDict={}
    for num in iList:
        if num not in iDict:
            iDict[num] = 1
        else:
            return True
    return False

def singleNumber_back(iList):
    iDict={}
    for num in iList:
        if num not in iDict:
            iDict[num] = 1
        else:
            del iDict[num]
    return iDict.popitem()[0]

def singleNumber(iList):
    cList=[]
    n = 0
    for num in iList:
        n ^= num
        cList.append(n)
    print (cList)
    return n

def intersect(l1,l2):
    result = []
    iDict={}
    for num in l1:
        if num not in iDict:
            iDict[num] = 1
        else:
            iDict[num] += 1

    for num in l2:
        if (num in iDict) and iDict[num] >=  1:
            iDict[num] -= 1
            result.append(num)

    return result

def plusOne(iList):
    flag = True
    for i in range(len(iList)-1,-1,-1):
        if flag:
            if iList[i] ==  9:
                iList[i] = 0
            else:
                iList[i] += 1
                flag = False
    if flag :
        iList.insert(0,1)

    return iList

def moveZero_back(iList):
    left = 0
    right  = len(iList) -1
    while right - left >=1:
        if iList[left] == 0 and iList[right] != 0 :
            iList[left],iList[right] = iList[right],iList[left]

        while iList[left] != 0:
            left += 1
        while iList[right] == 0:
            right -= 1
    return iList

def moveZeros(iList):
    left = 0
    for i,num in enumerate(iList):
        if num != 0:
            if left < i:
                iList[left] = num
                iList[i] = 0
            left += 1
    return iList

def twoSum_back(iList,target):
    iDict = {}
    for i, num in enumerate(iList):
        if num not in iDict:
            iDict[num] = [i]
        else:
            iDict[num] += [i]
    print(iDict)
    for k,v in iDict.items():
        another = target - k
        if another == k and len(v) >= 2:
            return  v[:2]
        if another  != k and another in iDict:
            return [v[0],iDict[another][0]]

def twoSum(iList,target):
    print(iList)
    for i,num in enumerate(iList):
        another = target - num
        if another in iList[i+1:]:
            j  = iList[i+1:].index(another)
            return [i,j+i+1]

def rotate_matrix(matrix):
    iLen =  len(matrix)
    for i in range(iLen):
        for j in range(i+1 , iLen):
            matrix[i][j],matrix[j][i]    = matrix[j][i],matrix[i][j]
        matrix[i].reverse()
    return matrix

def main():
    from pythonds.test import randomList,doubleListRemoveOne,randomZero,randomMatrix,printMatrix
    from pythonds.sort import quickSort

    #iList = quickSort(randomList(20))
    iList = randomList(20)
    print(iList)
    #randomZero(iList,10)
    #iListSorted = quickSort(iList)
    #doubleList = doubleListRemoveOne(iList)
    #print(iList)
    #print(iListSorted)
    #print(doubleList)
    # l1 = randomList(20)
    # l2 = randomList(20)
    # l1Sorted = sorted(l1)
    # l2Sorted = sorted(l2)
    # print(l1)
    # print(l2)
    # print(l1Sorted)
    # print(l2Sorted)

    # length = removeDuplicates(iList)
    # print("new list is {} len is {}".format(iList[:length] , length))

    # profit =  maxProfit_back(iList)
    # print("profit back  is {}".format(profit))
    # profit = maxProfit(iList)
    # print("profit is {}".format(profit))

    # print("iList is {}".format(rotate(iList,3)))

    #print("containsDuplicate is {}".format(containsDuplicate(iList)))

    #print("singleNumber is {}".format(singleNumber(doubleList)))

    #print("intersect is {}".format(intersect(l1,l2)))

    #print (plusOne([1,9,9]))

    #print("moveZero is {}".format(moveZeros(iList)))
    #print(moveZeros(iList))

    # print(twoSum([50, 50, 48, 95, 10, 18, 32, 15, 12, 20, 7, 17, 57, 22, 19, 74, 22, 12, 46, 40],100))
    # print(twoSum(iList, 100))

    matrix = randomMatrix(3)
    printMatrix(matrix)
    printMatrix(rotate_matrix(matrix))

if __name__ == "__main__":
    main()

