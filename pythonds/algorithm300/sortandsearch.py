#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: sortandsearch.py
@time:  19:18
@welcom to learn ai
"""


def quickSort(self, iList, start, end):
    if start >= end:
        return
    l = start + 1
    r = end
    while r >= l:
        while r >= l and iList[start] <= iList[r]:
            r -= 1
        while r >= l and iList[start] >= iList[l]:
            l += 1
        if r > l:
            iList[l], iList[r] = iList[r], iList[l]
    # if iList[start] < iList[r]:
    #    r -= 1
    iList[start], iList[r] = iList[r], iList[start]

    self.quickSort(iList, start, r - 1)
    self.quickSort(iList, r + 1, end)
    return iList

def binary_search(self,nums,q):
    left = 0
    right = len(nums) - 1
    while right - left > 1:
        mid  =  (left + right) // 2
        if nums[mid] < q:
            left  = mid
        else:
            right = mid
    if nums[left] >= q:
        return left
    if nums[right] >= q:
        return right
    return right + 1