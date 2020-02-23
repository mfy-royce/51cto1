#!/usr/bin/python
# encoding: utf-8

"""
author:Royce
contact:mfy-111@163.com
@file: mathematics.py
@time:  12:19
@welcom to learn ai
"""


class Solution():

    """
    完全平方数 1,4,9,16,25,,,,,,,
    1   1
    2   11
    3   111
     4   4
    5   41
    6   411
    7   4111
     8   44
    9   9
    10  91
    11  911
     12  444
    13  94
    14  941
    15  9411
     16  16
    17  161
    18  1611
    19  16111
     20  164
    21  1641
    22  994
    23  9941
    24  1644
    25  25


    """
    def  numSquares(self,n):
        for i in range(n+1):
            temp =  i * i
            if temp<=n:
                if int((n-temp) ** 0.5) ** 2 + temp ==n:
                    return 1+ 0 if temp ==0 else 1
            else:
                break
        if n % 8 == 7:
            return 4
        return 3

    def isPerfectSquare(self,num):
        l = 0
        r = num
        while r - l > 1:
            mid = (r + l)//2
            if mid * mid <num:
                l = mid
            else:
                r = mid
        if r * r == num:
            return True
        if l * l ==num:
            return True
        return False

    def isPowerOf2(self,n):
        while n % 2 == 0:
            n //= 2
        if n==1:
            return True
        else:
            return False

    def sqrt(self,n):
        l = 0
        r = n
        while r - l > 1:
            mid = (r+l) //2
            if mid * mid > n:
                r = mid
            else:
                l = mid
        if l * l  == n:
            return l
        if r * r  == n:
            return r
        return l

    def myPower(self,x,n):
        if x == 0 and  n == 0 :
            return -1
        if x  == 0 :
            return 0
        if n == 0:
             return 1
        if n<0:
            x = 1 / x
            n  = - n
        power = 1
        for i in range(1,n+1):
            power *=x
        return power

    def poww(self,a,b):
        ans = 1
        while b !=0:
            if b & 1 !=0:
                ans *= a
            a *=a
            b >>=1
        return ans

    def fastPower(self,a,b,x):
        return self.poww(a,b) % x




    def bitSwapRequired(self,a,b):
        c =  a^ b
        count =0
        while c!= 0:
            if c & 1 != 0:
                count +=1
            c >>= 1
        return count

    def romanToInt(self,s):
        if len(s) ==0:
            return 0
        index= len(s)-2
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum  = roman[s[-1]]
        while index >= 0:
            if roman[s[index]] < roman[s[index+1]]:
                sum -= roman[s[index]]
            else:
                sum += roman[s[index]]
            index -= 1
        return  sum

    def intToRoman(self,n):
        numDict ={
            1:"I",
            2:"II",
            3:"III",
            4:"IV",
            5:"V",
            6:"VI",
            7:"VII",
            8:"VIII",
            9:"IX",
        }
        romanDict ={
            "I":["I","X","C","M"],
            "V":["V","L","D","?"],
            "X":["X","C","M","?"]
        }
        s = ""
        index= 0
        while n > 0:
            num = n % 10
            if num != 0:
                s =  numDict[num].replace("X",romanDict["X"][index]).replace("V",romanDict["V"][index]).replace("I",romanDict["I"][index]) + s
            n //= 10
            index += 1
        return s

    def quickSort(self,iList,start,end):
        if start >= end:
            return
        l = start+1
        r = end
        while r>=l:
            while r>=l and iList[start] <= iList[r]:
                r -= 1
            while r >=l and iList[start] >= iList[l]:
                l += 1
            if r > l:
                iList[l],iList[r] = iList[r],iList[l]
        #if iList[start] < iList[r]:
        #    r -= 1
        iList[start], iList[r] = iList[r], iList[start]

        self.quickSort(iList,start,r-1)
        self.quickSort(iList,r+1,end)
        return iList

    def integerReplacement(self,n):
        memo={}
        self.dfs(n,memo)
        print(memo[n])
        return len(memo[n])-1

    def dfs(self,n,memo):
        if n == 1:
            memo[n] = [1]

        if n in memo:
            return memo[n]

        temp = []
        if n % 2 == 0:
            temp.append(n)
            cur = self.dfs(n//2,memo)
            temp.extend(cur)
            memo[n] = temp
            return  temp
        else:
            temp2 =  temp.copy()
            temp.append(n)
            cur = self.dfs(n +1, memo)
            temp.extend(cur)

            temp2.append(n)
            cur2 =self.dfs(n -1 ,memo)
            temp2.extend(cur2)

            if len(temp) < len(temp2):
                memo[n] = temp
                return temp
            else:
                memo[n]= temp2
                return temp2

def main():
    from pythonds.test import randomList,sortVerify
    # iList= randomList(30)
    #iList = [87, 61, 4, 2, 64]
    #iList =[4, 86, 4, 24, 0]
    #iList = []
    #iList =[10, 70, 14, 48, 28, 85, 8]
    #iList =[81, 11, 31, 18, 8, 81, 85, 81, 77]
    # print("iList is {}".format(iList))

    solution = Solution()
    # print("result is {}".format(solution.numSquares(12)))
    # print("isPerfectSquare is {}".format(solution.isPerfectSquare(4)))
    # print("isPowerOf2 is {}".format(solution.isPowerOf2(1)))
    # print("sqrt is {}".format(solution.sqrt(1)))
    # print("myPower is {}".format(solution.myPower(2,-2)))
    #
    # print("fastPower is {}".format(solution.fastPower(2,31,3)))
    #
    # print("bitSwapRequired is {}".format(solution.bitSwapRequired(10 ,26)))
    #
    # print("romanToInt is {}".format(solution.romanToInt('XX')))
    #
    # print("intToRoman is {}".format(solution.intToRoman(99)))

    # print("quickSort is {}".format(solution.quickSort(iList,0,len(iList)-1)))

    # def sortVerify(n,length,sortFunc):
    #     iList = randomList(10)
    #     sortedList  = sortFunc(iList, 0, len(iList) - 1)

    sortVerify(1000,20,solution.quickSort)

    print("integerReplacement is {}".format(solution.integerReplacement(18)))


if __name__ == "__main__":
    main()

