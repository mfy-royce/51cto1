#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: preprocessor.py
@time:  0:38
@welcom to learn ai
"""


def readDict(path):
    with open(path, 'r', encoding="utf-8") as f:
        list1 = f.readlines()
        list2 = [i.rstrip("\n") for i in list1]
        return set(list2)


def forwardMatch(iDict, s):
    for i in range(len(s) - 1, -1, -1):
        if s in iDict:
            return i
        s = s[:-1]
    return -1


def forwardMaximumMatch(iDict, maxlength, s):
    result = []
    while len(s) > 0:
        subS = s[:maxlength]
        index = forwardMatch(iDict, subS)
        if index == -1:
            s = s[1:]
            result.append(s[0])
        else:

            result.append(s[:index + 1])
            s = s[index + 1:]
    return result


def reverseMatch(iDict, s):
    for i in range(len(s)):
        if s in iDict:
            return i
        s = s[1:]
    return -1


def reverseMaximumMatch(iDict, maxlength, s):
    result = []
    while len(s) > 0:
        subS = s[-maxlength:]
        index = reverseMatch(iDict, subS)
        if index == -1:
            s = s[:-1]
            result.append(s[-1])
        else:
            result.append(s[index - len(subS):])
            s = s[:index - len(subS)]
    return result[::-1]


def biMaximumMatch(iDict, maxlength, s):
    forResult = forwardMaximumMatch(iDict, maxlength, s)
    forSingleWord = 0
    for word in forResult:
        if len(word) == 1:
            forSingleWord += 1

    revResult = reverseMaximumMatch(iDict, maxlength, s)
    revSingleWord = 0
    for word in revResult:
        if len(word) == 1:
            revSingleWord += 1

    if forResult == revResult:
        return forResult
    if len(forResult) == len(revResult):
        if forSingleWord < revSingleWord:
            return forResult
        else:
            return revResult

    if len(forResult) > len(revResult):
        return revResult
    else:
        return forResult


def main():
    wordSet = readDict('worddict.txt')
    print(wordSet)
    cutResult = forwardMaximumMatch(wordSet, 5, "北京大学生前来应聘")
    print(cutResult)
    cutResult = reverseMaximumMatch(wordSet, 5, "北京大学生前来应聘")
    print(cutResult)
    cutResult = biMaximumMatch(wordSet, 5, "北京大学生前来应聘")
    print(cutResult)


if __name__ == "__main__":
    main()
