#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lcothers.py
@time:  0:03
@welcom to learn ai
"""

def hammingWeight(n):
    bList = list(bin(n))
    sum =  0
    for i in bList:
        if i == "1":
            sum += 1
    print(bList)
    return sum

def hammingDistance(x,y):
    xList = list(bin(x))[2:]
    yList = list(bin(y))[2:]
    if len(xList) < 31:
        xList = ["0"]* (31 -len(xList)) + xList
    if len (yList) < 31:
        yList = ["0"] * (31 -len(yList)) + yList
    distance = 0
    for i in range(31):
        if xList[i] != yList[i]:
            distance += 1
    return distance


def reverseBit(n):
    dec2bin = bin(n)[2:]
    newBin = dec2bin[::-1]
    if len(newBin) < 32 :
        newBin  = newBin + '0' *(32 -  len (newBin ))
        newDec = int(newBin,2)
    return newDec


def generate(numRows):
    rList =[1]
    iList = [rList.copy()]
    for i in range(1,numRows):
        rList.insert(0,0)
        for j,num in  enumerate(rList[:i]):
            rList[j] += rList[j+1]
        iList.append(rList.copy())
    return iList

def isValid(s):
    stack = []
    iDict ={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for i in s:
        if i ==')' or i =="]" or i == "}":
            if len(stack) ==0 :
                return False
            elif iDict[i] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if len(stack) == 0:
        return  True
    else:
        return False

def missingNumber(iList):
    iSet = set(iList)
    for i in range(len(iList)+1):
        try:
            iSet.remove(i)
        except:
            return i

def main():
    import  timeit
    print('hammingWeight is {}'.format(hammingWeight(0b0000000000000000000001011)))

    print('hammingDistance is {}'.format(hammingDistance(1,4)))

    print('reverseBit is {}'.format(reverseBit(43261596)))

    print('generate is {}'.format(generate(5)))

    print('isValid is {}'.format(isValid("abc{}[]")))

    print('missingNumber is {}'.format(missingNumber([9,6,4,2,3,5,7,0,1])))


    # print('countPrimesV1 is {}'.format(countPrimesV1(10000)))
    # print(timeit.timeit("countPrimesV1(10000)","from __main__ import countPrimesV1",number=10))
    #
    # print('countPrimesV2 is {}'.format(countPrimesV2(10000)))
    # print(timeit.timeit("countPrimesV2(10000)","from __main__ import countPrimesV2",number=10))

    #print('isPowerOfThree is {}'.format(isPowerOfThree(pow(3,19))))


if __name__ =="__main__":
    main()