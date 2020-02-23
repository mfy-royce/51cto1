#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: string.py
@time:  13:58
@welcom to learn ai
"""

def reverseString(s):
    left = 0
    right = len(s) -1
    while  right - left >0:
        s[left],s[right] =s[right],s[left]
        right -= 1
        left += 1
    return s

def reverseInt(x):
    y = 0
    while x != 0:
        y =  y *10 + (x % 10)
        x =  x // 10
    return y


def firstUniqChar(s):
    iDict = {}
    head = [None,None,None,None]
    end = head
    print("test")

    def addNewNode(c):
        iDict[c] = [i, 1, end, None, c]
        end[3] = iDict[c]
        return iDict[c]

    def deleteNode(c):
        iDict[c][2][3] = iDict[c][3]
        if iDict[c][3] != None:
            iDict[c][3][2] = iDict[c][2]
        return iDict[c]

    def addOldNode(c):
        iDict[c][1] += 1
        iDict[c][2] = end
        iDict[c][3] = None
        end[3] = iDict[c]
        return iDict[c]



    for i,c in enumerate(s):
        if c not in iDict:
            end = addNewNode(c)
        else:
            deleteNode(c)
            if iDict[c] == end:
                end = iDict[c][2]
            end = addOldNode(c)

    index = head[3][0]
    return head,index



def isAnagram(s,t):
    def dictCount(s):
        iDict = {}
        for i, char in enumerate(s):
            if char not in iDict:
                iDict[char] = 1
            else:
                iDict[char] += 1
        return iDict

    iDict = dictCount(s)
    for char in t:
        if char not in iDict:
            return False
        else:
            iDict[char] -= 1
            if iDict[char] == 0:
                del iDict[char]
    if len(iDict) == 0:
        return True
    return False

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    while right - left > 0:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -=1
            continue

        if s[right] == s[left]:
            right -= 1
            left += 1
        else:
            return False
    return  True


def atoi(s):

    s= s.strip()
    if len(s) == 0 :
        return -1
    if s[0] == '-' and not s[1].isnumeric():
        return -1
    elif not s[0].isnumeric() and s[0] != "-":
        return -1

    if s[0] =='-':
        flag =-1
        s= s[1:]
    else:
        flag = 1
    #s =  s[::-1]
    sum =0
    for i in s:
        if i.isnumeric():
            sum = sum* 10 + int(i)
        else:
            break

    sum = sum *flag
    if sum> pow(2,31)-1:
        sum = pow(2,31)-1
    elif sum < -pow(2,31):
        sum = -pow(2,31)
    return sum*flag

def strStr(haystack,needle):
    if len(neele) ==  0 :
        return  0
    if len(haystack)  < len(needle):
        return -1
    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i:i+len(needle)] == needle:
            return i
        i += 1
    return -1


def countAndSay(s):
    iLen = len(s)

    pCurrent = 1
    char_last = s[0]
    count  =  1
    newS = ""
    while pCurrent < iLen:
        if char_last ==  s[pCurrent]:
            count += 1
        else:
            newS += str(count) + char_last
            count =1
            char_last = s[pCurrent]
        pCurrent +=1
    newS += str(count) + char_last
    return newS

def countAndSanN(n):
    i= 1
    while i <= n:
        if i ==1:
            s = "1"
        else:
            s= countAndSay(s)
        print("countAndSan {} is {}".format(i,s) )
        i+= 1

def longestCommonPrefix(iList):
    if len(iList) <1:
        return ""
    if len(iList) ==1:
        return iList[1]
    minLen = len(iList[0])
    #minIndex = 0
    for i,s in enumerate(iList):
        if minLen > len(s):
            minLen= len(s)
            #minIndex = i
    #minLenNum =  iList[minIndex]

    for i in range(minLen):
        char = iList[0][i]
        for s in iList:
            if s[i] !=char:
                return iList[0][:i]
    return iList[0][:minLen]

def main():
    from pythonds.test import printLink

    # strList = list("hello")
    # print(strList)
    # reverseStrList = "".join(reverseString(strList))
    # print(reverseStrList)
    #print(reverseInt(1230))


    # head,index = firstUniqChar("leetcodelct")
    # printLink(head)
    # print('index is {}'.format(index))
    #
    # print('isAnagram is {}'.format(isAnagram("anagram","nagadam")))

    # print('isPalindrome is {}'.format(isPalindrome("A man, a plan, a canal: Panama")))

    #print("atoi is  {}".format(atoi( str(pow(2,31))   )))

    #print("strStr is {}".format(strStr("hello","ll")))

    #countAndSanN(30)
    #print("countAndSay is {}".format(countAndSay()))

    print("longestCommonPrefix is {}".format(longestCommonPrefix(["flower","flow","flight","f"])))
if __name__ == "__main__":
    main()


