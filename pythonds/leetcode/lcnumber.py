#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: lcnumber.py
@time:  15:10
@welcom to learn ai
"""
def fizzBuzz(n):
    rList = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0:
            rList.append("FrizzBuzz")
        elif i % 3 == 0:
            rList.append("Fizz")
        elif i % 5 == 0:
            rList.append("Buzz")
        else:
            rList.append(str(i))
    return  rList

def countPrimesV1(n):
    primes = []
    for i in range(2,n):
        primeFlag = True
        for j in range(2,i):
            if i % j ==0:
                primeFlag = False
        if primeFlag:
            primes.append(i)
    print(primes)
    return  len(primes)

def countPrimesV2(n):
    iList = [True for i in range(n)]

    for i in range(2,int(pow(n,0.5))+1):
        if iList[i]:
            iList[i+i::i] =[False] * len(iList[i+i::i])

    rList = [i for i,flag in enumerate(iList) if i>=2 and flag==True ]
    print(rList)
    return len(rList)

def isPowerOfThree(n):
    flag= True
    while n > 3:
        if n % 3 != 0:
            flag = False
            break
        n = n//3
    if  n != 3:
        flag = False
    return flag


def romanToInt(s):
    romanDict={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    doubleDict={
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900,
    }
    sum = 0
    i  = 0
    while i <len(s) :
        try:
            s[i:i+2]
        except IndexError as e:
            sum += romanDict[s[i]]
            i += 1
        else:
            if s[i:i+2] in doubleDict.keys():
                sum += doubleDict[s[i:i+2]]
                i += 2
            else:
                sum += romanDict[s[i]]
                i += 1
    return  sum

def main():
    import  timeit
    # print('fizzBuzz is {}'.format(fizzBuzz(15)))

    # print('countPrimesV1 is {}'.format(countPrimesV1(10000)))
    # print(timeit.timeit("countPrimesV1(10000)","from __main__ import countPrimesV1",number=10))
    #
    # print('countPrimesV2 is {}'.format(countPrimesV2(10000)))
    # print(timeit.timeit("countPrimesV2(10000)","from __main__ import countPrimesV2",number=10))

    #print('isPowerOfThree is {}'.format(isPowerOfThree(pow(3,19))))

    print('romanToInt is {}'.format(romanToInt("MCMXCIV")))
if __name__ =="__main__":
    main()