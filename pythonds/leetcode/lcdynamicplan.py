#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lcdynamicplan.py
@time:  19:58
@welcom to learn ai
"""

def climbStairs_back(n):
    if n<= 0:
        return -1
    if n == 1:
        return 1

    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

def climbStairs(n):
    iList= [1,1,2]
    i =3
    while i<=n:
        iList.append(iList[i-1] + iList[i-2])
        i += 1
    return iList[n]

def maxProfit(iList):
    profit  = 0
    for i in range(len(iList) - 1):
        sub= max(iList[i+1:]) -iList[i]
        profit = max(sub,profit)
    return profit


def rob(nums):
    maxcash=[nums[0],max(nums[0],nums[1])]
    for i in range(2,len(nums)):
        maxcash.append(max(maxcash[i-2]+nums[i],maxcash[i-1]) )
    return maxcash[len(nums)-1]


def main():
    print('climbStairs is {}'.format(climbStairs(5)))

    print('maxProfit is {}'.format(maxProfit([7,1,5,3,6,4])))

    print('rob is {}'.format(rob([1,2,3,3])))

if __name__ =="__main__":
    main()
